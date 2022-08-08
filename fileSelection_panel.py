
from pathlib import PurePath
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal,SIGNAL)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent,QKeyEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout, QListWidgetItem,QTableWidget,QListWidget)
import pyqtgraph as pg
from fileSelection_panel_ui import Ui_FileSelectionPanel 
from widget_manipulation_class import WidgetData, MousePressEvent, VariableItemObject
from variable_panel import VariablePanel
from file_manager import FileManager as FM
from pyqtgraph.parametertree import Parameter
import os
from CustomTableWidget import fileSelectionTableWidget
from CustomQMenu import FileSelectionQMenu
class FileSelectionPanel(Ui_FileSelectionPanel,QWidget):
    signal_doubleClicked_listwidget = Signal(object)
    sendData_signal = Signal(object)

    def __init__(self,parent=None):
        super(FileSelectionPanel, self).__init__(parent)                
        self.setupUi(self)  # Generate UI
        self.connectSignal() # Connect signals
        self.setupContextMenu() 
        # File list stored in a Parameter
        self._fileList_Parameters = Parameter.create(name='file_list',title='File List',type='group',children=[])

    def setupContextMenu(self):
        # ContextQMenu for fileSelection_listWidget (Should be moved in a subclass of listWidget)
        self.fileSelection_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fileSelection_listWidget.connect(self.fileSelection_listWidget,SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)
        self.fileListSelection_QMenu = FileSelectionQMenu(selection=bool(self.fileSelection_listWidget.selectedItems()))        
        self.fileListSelection_QMenu.QActionOperation_signal.connect(self.readQMenuSignal)        

    def getData(self,format,function):        
        data = self.importDataFromFile(format)        
        self.sendData_signal.emit(data,function)
            
    def importDataFromFile(self,format):
        for item in self.fileSelection_listWidget.selectedItems():
            data = FM(self._fileList_Parameters.child(item.text())['fullpath'],format).readFile()
            return Parameter.create(name=item.text(),value=data)

    def storeFiles(self,filename_list):
        [self.storeFile(filename) for filename in filename_list]              


    def updateParameterTree(self,):
    
        P = self._fileList_Parameters.child(self.fileSelection_listWidget.currentItem().text())
        self.fileDes_parameterTree.clear()
        [self.fileDes_parameterTree.addParameters(child,showTop=True) for child in P.childs]        
        # self.fileAttr_parameterTree.setParameters(P,showTop=False)
        # self.filePrev_parameterTree.setParameters(P,showTop=True)

    def storeFile(self,filename_fullpath):
        P = FM(filename_fullpath).makeParameter()
        # Add child to parameter
        self._fileList_Parameters.addChild(P)
        # Add entry to list
        self.addEntry(QListWidgetItem(P.name()))

    def showfileDetails(self):
        if self.showDetails_checkBox.isChecked():
            self.fileDetails_tabwidget.show()
        else:
            self.fileDetails_tabwidget.hide()
    ################################################## Context menu ##########################################    
    def listItemRightClicked(self, QPos): 
        self.fileListSelection_QMenu.updateSelection(self.fileSelection_listWidget.selectedItems())
        parentPosition = self.fileSelection_listWidget.mapToGlobal(QPoint(0, 0))        
        self.fileListSelection_QMenu.move(parentPosition + QPos)
        self.fileListSelection_QMenu.show() 
    ################################################## Read Context menu ##########################################    
    def readQMenuSignal(self,input):
        if input  == 'openMBES':
            self.getData('MBES','open')
        elif input  == 'oxtractMBES':
            self.getData('MBES','store')            
        elif input == 'saveData':
            print('Saving data... or not')
        elif input == 'removeItems':
            self.removeSelectedItems()
        elif input == 'clearList':                        
            self.fileSelection_listClearItemClicked()
    ################################################## Context menu functions ##########################################    
    
    def fileSelection_listClearItemClicked(self):
        [self.removeEntry(item) for item in self.selectAllItems()]
    def fileSelection_listRemoveItemClicked(self):
        self.removeSelectedItems()


    ################################################## Connect Signal ##########################################    
    def connectSignal(self):  
        # Connect signals for FileSelectionPanelWidget
        self.makeInput_pushButton.clicked.connect(self.press_makeButton_function)
        self.fileSelection_listWidget.itemDoubleClicked.connect(self.doubleClicked_listWidget_function)
        self.showDetails_checkBox.stateChanged.connect(self.showfileDetails)
        self.fileSelection_listWidget.itemSelectionChanged.connect(self.updateParameterTree)
    ################################################## Functions ##########################################    

    def addEntry(self,item):
        # Add a new entry to FileSelectionPanel containing item
        self.fileSelection_listWidget.addItem(item)
        self.fileSelection_listWidget.clearSelection()
        self.fileSelection_listWidget.setCurrentItem(item)

    def removeEntry(self,item):
        self._fileList_Parameters.removeChild(self._fileList_Parameters.child(item.text())) # Remove item from parameters
        self.fileSelection_listWidget.takeItem(self.fileSelection_listWidget.row(item))  # Remove item from list

    def removeSelectedItems(self):
        [self.removeEntry(item) for item in self.fileSelection_listWidget.selectedItems()]
        
    def selectAllItems(self):
        return [self.fileSelection_listWidget.item(row) for row in range(self.fileSelection_listWidget.count())]

    def clearAll(self):
        [self.removeEntry(item) for item in self.selectAllItems()]
    ################################################## Signal from action ##########################################    
        
    def press_makeButton_function(self,input = None):
        # Make item in FileSelectionPanel       
        P = FM('analysis_functions.py').makeParameter()        
        self._fileList_Parameters.addChild(P)
        self.addEntry(QListWidgetItem(P.name()))


    def doubleClicked_listWidget_function(self,item):
        # Send signal to VariablePanelWidget to create and/or set tab in VariablePanelWidget associated to item
        self.signal_doubleClicked_listwidget.emit(item)


def main():
    app = QApplication([])
    widget = FileSelectionPanel()
    widget.show()
    app.exec()
if __name__=="__main__":
    main()
