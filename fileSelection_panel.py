
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
from file_manager import FileManager
# Panel containing datalistItem

class FileSelectionPanel(Ui_FileSelectionPanel,QWidget):
    signal_loadButton = Signal()
    signal_makeButton = Signal()
    signal_doubleClicked_listwidget = Signal(object)
    signal_deleteButton = Signal()
    signal_removeEntry = Signal(object)
    signal_sendData = Signal(object)
    def __init__(self,parent=None):
        super(FileSelectionPanel, self).__init__(parent)                
        self.setupUi(self)  # Generate UI
        self.connectSignal() # Connect signals
        # self.widget_data = WidgetData(self,variableItemParameters= True) # Gives method WidgetData to FileSelectionPanel
        self.setupWindows() 

    def setupWindows(self):
        # Initialize a VariablePanelWidget to read entry in FileSelectionPanel (given as Data_listItem)
        self.variableTable_panel = VariablePanel()  # Create VariablePanel
        self.connectVariablePanelSignal()
        self.fileSelection_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fileSelection_listWidget.connect(self.fileSelection_listWidget,SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)


    ################################################## Context menu ##########################################    

    def listItemRightClicked(self, QPos): 
        self.listMenu= QMenu()
        self.connect(self.listMenu.addAction("Add Item"),SIGNAL("triggered()"), self.fileSelection_listAddItemClicked)
        self.connect(self.listMenu.addAction("Show Item(s)"),SIGNAL("triggered()"), self.fileSelection_listShowItemClicked) 
        self.connect(self.listMenu.addAction("Copy Item(s)"),SIGNAL("triggered()"), self.fileSelection_listCopyItemClicked) 
        self.connect(self.listMenu.addAction("Remove Item(s)"),SIGNAL("triggered()"), self.fileSelection_listRemoveItemClicked) 
        self.connect(self.listMenu.addAction("Clear all"),SIGNAL("triggered()"), self.fileSelection_listClearItemClicked) 

        parentPosition = self.fileSelection_listWidget.mapToGlobal(QPoint(0, 0))        
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show() 

    ################################################## Context menu functions ##########################################    
    def fileSelection_listShowItemClicked(self):
        [self.signal_doubleClicked_listwidget.emit(item) for item in self.fileSelection_listWidget.selectedItems()]

    def fileSelection_listCopyItemClicked(self):
        [self.copyEntry(item) for item in self.fileSelection_listWidget.selectedItems()]

    def fileSelection_listRemoveItemClicked(self):
        self.removeSelectedItems()

    def fileSelection_listAddItemClicked(self):
        self.addEntry(Data_listItem(f'{self.fileSelection_listWidget.count()}'))

    def fileSelection_listClearItemClicked(self):
        [self.removeEntry(item) for item in self.selectAllItems()]

    ################################################## Connect Signal ##########################################    

    def connectSignal(self):  
        # Connect signals for FileSelectionPanelWidget
        # self.deleteInput_pushButton.clicked.connect(self.press_deleteButton_function)
        self.makeInput_pushButton.clicked.connect(self.press_makeButton_function)
        # self.loadInput_pushButton.clicked.connect(self.press_loadButton_function)
        self.fileSelection_listWidget.itemDoubleClicked.connect(self.doubleClicked_listWidget_function)

    def connectVariablePanelSignal(self):
        # Connect signals for VariablePanelWidget
        self.signal_removeEntry.connect(self.variableTable_panel.closeTab_fromWidget_function)
        self.signal_doubleClicked_listwidget.connect(self.variableTable_panel.setTab_fromWidget_function)

    ################################################## Functions ##########################################    
    def addEntries(self,items):
        [self.addEntry(QListWidgetItem(item)) for item in items]
        [self.addEntry(Data_listItem(item)) for item in items]

    def addEntry(self,item):
        # Add a new entry to FileSelectionPanel containing item
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.fileSelection_listWidget.addItem(item)
        self.fileSelection_listWidget.clearSelection()
        self.fileSelection_listWidget.setCurrentItem(item)

    def copyEntry(self,item):
        # Add a new entry to FileSelectionPanel containing item
        self.addEntry(Data_listItem(f'{item.text()}_copy'))
    def removeEntry(self,item):
        # Remove entry to FileSelectionPanel + send signal to remove associated tab in VariablePanelWidget
        self.signal_removeEntry.emit(item.get_widgetDataVariableItem())
        self.fileSelection_listWidget.takeItem(self.fileSelection_listWidget.row(item)) 
        self.fileSelection_listWidget.setCurrentRow(self.fileSelection_listWidget.count()-1)

    def removeSelectedItems(self):
        [self.removeEntry(item) for item in self.fileSelection_listWidget.selectedItems()]

    def selectAllItems(self):
        return [self.fileSelection_listWidget.item(row) for row in range(self.fileSelection_listWidget.count())]

    ################################################## Signal from action ##########################################    

    def press_deleteButton_function(self):
        # Delete selected items
        self.removeSelectedItems()

    def press_loadButton_function(self):
        # Load item in FileSelectionPanel        
        self.path = str(QFileDialog.getOpenFileName(self,'Choose File','/home/cs268225/Documents/Python/GUI/FourierGUI/TestData/')[0])    
        if self.path:
            self.signal_loadButton.emit()        
            self.addEntry(Data_listItem(path = self.path))

        
    def press_makeButton_function(self,input = None):
        # Make item in FileSelectionPanel        
        if input:
            self.addEntry(Data_listItem(f'{input}'))
        else:
            self.addEntry(Data_listItem(f'{self.fileSelection_listWidget.count()}'))

        self.signal_makeButton.emit()

    def doubleClicked_listWidget_function(self,item):
        # Send signal to VariablePanelWidget to create and/or set tab in VariablePanelWidget associated to item
        self.signal_doubleClicked_listwidget.emit(item)

    def sendData(self):
        self.signal_sendData.emit([item.file_reader for item in self.fileSelection_listWidget.selectedItems()])

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
