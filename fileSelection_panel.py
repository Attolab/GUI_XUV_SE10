
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
    signal_loadButton = Signal()
    signal_makeButton = Signal()
    signal_doubleClicked_listwidget = Signal(object)
    signal_deleteButton = Signal()
    signal_removeEntry = Signal(object)
    sendData_signal = Signal(object)
    
    def __init__(self,parent=None):
        super(FileSelectionPanel, self).__init__(parent)                
        self.setupUi(self)  # Generate UI
        self.connectSignal() # Connect signals
        # self.widget_data = WidgetData(self,variableItemParameters= True) # Gives method WidgetData to FileSelectionPanel
        self.setupWindows() 
        self.fileList_Parameters = Parameter.create(name='file_list',title='File List',type='group',children=[])


    def setupWindows(self):
        # Initialize a VariablePanelWidget to read entry in FileSelectionPanel (given as Data_listItem)
        self.variableTable_panel = VariablePanel()  # Create VariablePanel
        self.connectVariablePanelSignal()
        self.fileSelection_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fileSelection_listWidget.connect(self.fileSelection_listWidget,SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)
        # self.fileSelection_ParameterTree = Parameter.create(name ='file_list',title='File List',type='group',expandable=True,)
        # self.fileSelection_tree.setHeaderHidden(True)
        # self.fileSelection_tree.addParameters(self.fileSelection_ParameterTree,showTop=False)        
    def getData(self,format):        
        data = self.importDataFromFile(format)
        self.sendData_signal.emit(data)

    def importDataFromFile(self,format):
        return [FM(self.fileList_Parameters.child(item.text())['fullpath'],format).readFile() for item in self.fileSelection_listWidget.selectedItems()]


    def storeFiles(self,filename_list):
        [self.storeFile(filename) for filename in filename_list]              

    def storeFile(self,filename_fullpath):
        folder,filename_withext = os.path.split(filename_fullpath)
        filename,ext = os.path.splitext(filename_withext)
        size = os.path.getsize(filename_fullpath)
        file_params =  {
                'fullpath':{
                    'title': 'filename',
                    'type': 'str',
                    'value': filename_fullpath,
                    'editable':False,
                    },               
                'dir': {
                    'title': 'folder',                                        
                    'type': 'str',
                    'value': folder,
                    'editable':False,
                    },   
                'ext': {
                    'title':'ext',                                        
                    'type': 'str',
                    'value': ext,
                    'editable':False,                    
                    },    
                'size': {
                    'title':'size',                                        
                    'type': 'int',
                    'value': size,
                    'editable':False,                    
                    },      
        }
        # Add entry to list
        self.addEntry(QListWidgetItem(filename_withext))
        # Add child to parameter
        self.fileList_Parameters.addChild(Parameter.create(name=filename_withext, type='group',expanded = False,children = file_params,removable = True,renamable=False))


    ################################################## Context menu ##########################################    
    def listItemRightClicked(self, QPos): 
        self.fileListSelection_QMenu = FileSelectionQMenu(selection=self.fileSelection_listWidget.selectedItems())        
        self.fileListSelection_QMenu.removeItem_signal.connect(self.removeSelectedItems)
        self.fileListSelection_QMenu.clearTable_signal.connect(self.fileSelection_listClearItemClicked)
        self.fileListSelection_QMenu.QActionOperation_signal.connect(self.readQMenuSignal)
        parentPosition = self.fileSelection_listWidget.mapToGlobal(QPoint(0, 0))        
        self.fileListSelection_QMenu.move(parentPosition + QPos)
        self.fileListSelection_QMenu.show() 
    ################################################## Read Context menu ##########################################    
    def readQMenuSignal(self,input):
        if input  == 'ExtractMBES':
            self.getData('MBES')
        elif input == 'SaveData':
            print('Saving data... or not')
        elif input == 'RemoveItems':
            self.removeSelectedItems()
        elif input == 'clearList':                        
            self.fileSelection_listClearItemClicked()
    ################################################## Context menu functions ##########################################    
    def fileSelection_listShowItemClicked(self):
        [self.signal_doubleClicked_listwidget.emit(item) for item in self.fileSelection_listWidget.selectedItems()]

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

    def showfileDetails(self):
        if self.showDetails_checkBox.isChecked():
            self.fileDetails_tabwidget.show()
        else:
            self.fileDetails_tabwidget.hide()
    def connectVariablePanelSignal(self):
        # Connect signals for VariablePanelWidget
        self.signal_removeEntry.connect(self.variableTable_panel.closeTab_fromWidget_function)
        self.signal_doubleClicked_listwidget.connect(self.variableTable_panel.setTab_fromWidget_function)

    ################################################## Functions ##########################################    

    def addEntry(self,item):
        # Add a new entry to FileSelectionPanel containing item
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.fileSelection_listWidget.addItem(item)
        self.fileSelection_listWidget.clearSelection()
        self.fileSelection_listWidget.setCurrentItem(item)

    def removeEntry(self,item):
        # Remove entry to FileSelectionPanel + send signal to remove associated tab in VariablePanelWidget
        # self.signal_removeEntry.emit(item.get_widgetDataVariableItem())
        self.fileList_Parameters.removeChild(self.fileList_Parameters.child(item.text())) # Remove item from parameters
        self.fileSelection_listWidget.takeItem(self.fileSelection_listWidget.row(item))  # Remove item from list
        # self.fileSelection_listWidget.setCurrentRow(self.fileSelection_listWidget.count()-1)

    def removeSelectedItems(self):
        [self.removeEntry(item) for item in self.fileSelection_listWidget.selectedItems()]
        
    def selectAllItems(self):
        return [self.fileSelection_listWidget.item(row) for row in range(self.fileSelection_listWidget.count())]

    def clearAll(self):
        [self.removeEntry(item) for item in self.selectAllItems()]
    ################################################## Signal from action ##########################################    
        
    def press_makeButton_function(self,input = None):
        # Make item in FileSelectionPanel        
        if input:
            self.addEntry(fileSelection_listItem(f'{input}'))
        else:
            self.addEntry(fileSelection_listItem(f'{self.fileSelection_listWidget.count()}'))

        self.signal_makeButton.emit()

    def doubleClicked_listWidget_function(self,item):
        # Send signal to VariablePanelWidget to create and/or set tab in VariablePanelWidget associated to item
        self.signal_doubleClicked_listwidget.emit(item)

    # def sendData(self):
        # self.signal_sendData.emit([item.file_reader for item in self.fileSelection_listWidget.selectedItems()])


# Custom widget datalist item that has a subclass to access its data
class fileSelection_listItem(QListWidgetItem):

    def __init__(self, parent = None, name = 'Test_DataListItem', path = None) -> None:
        super(fileSelection_listItem, self).__init__(parent)   
        try:   
            if path:
                self.P = PurePath(path)
                self.file_reader = FileReader(self.P)
                self.setText(self.P.name)
            else:
                self.P = None
                self.file_reader = None
            self.widgetDataVariables = self.make_widgetDataVariables()
        except:
            pass


    def make_widgetDataVariables(self):
        return VariableItemObject(file_reader = self.file_reader)

    def get_widgetDataVariables(self):
            return self.widgetDataVariables

    def get_widgetDataVariableItem(self):
        return self.widgetDataVariables.get_VariableItemTable()

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_F2:
                self.emit(SIGNAL('MYSIGNAL'))
                print('Rename')



# Custom widget datalist item that has a subclass to access its data
class Data_listItem(QListWidgetItem):

    def __init__(self, parent = None, name = 'Test_DataListItem', path = None) -> None:
        super(Data_listItem, self).__init__(parent)   
        try:   
            if path:
                self.P = PurePath(path)
                self.file_reader = FileReader(self.P)
                self.setText(self.P.name)
            else:
                self.P = None
                self.file_reader = None
            self.widgetDataVariables = self.make_widgetDataVariables()
        except:
            pass


    def make_widgetDataVariables(self):
        return VariableItemObject(file_reader = self.file_reader)

    def get_widgetDataVariables(self):
            return self.widgetDataVariables

    def get_widgetDataVariableItem(self):
        return self.widgetDataVariables.get_VariableItemTable()

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_F2:
                self.emit(SIGNAL('MYSIGNAL'))
                print('Rename')

def main():
    app = QApplication([])
    widget = FileSelectionPanel()
    widget.show()
    app.exec()
if __name__=="__main__":
    main()
