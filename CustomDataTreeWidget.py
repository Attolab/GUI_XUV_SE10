
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,SIGNAL,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QTreeWidget,QTreeWidgetItem,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow,QHeaderView)
from CustomDataTreeWidget_ui import Ui_CustomDataTreeWidget
from CustomTableWidget import CustomTableWidget,fileSelectionTableWidget
from pyqtgraph import DataTreeWidget
import numpy as np
from CustomQMenu import DataSelectionQMenu

class CustomDataTreeWidget(Ui_CustomDataTreeWidget,QWidget):
    showVariable_signal = Signal(object)

    def __init__(self,parent = None,data = None):
        super(CustomDataTreeWidget, self).__init__(parent)         
        self.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate("CustomDataTreeWidget", u"Data Browser", None))        
        self.setupWindows()
        self.connectSignals()  

    def connectSignals(self):
        self.add_pushButton.pressed.connect(self.addEntry_pushButton)
        self.delete_pushButton.pressed.connect(self.removeEntry_pushButton)
        self.data_treeWidget.itemDoubleClicked.connect(self.doubleClicked_treeWidget_function)

    def setupWindows(self):
        self.data_treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.data_treeWidget.connect(self.data_treeWidget,SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)
        self.dataTreeWidget_QMenu = DataSelectionQMenu(selection=bool(self.data_treeWidget.selectedItems()))  
        self.dataTreeWidget_QMenu.QActionOperation_signal.connect(self.readQMenuSignal)        
        

    def listItemRightClicked(self,QPos):
        self.dataTreeWidget_QMenu.updateSelection(self.data_treeWidget.selectedItems())
        parentPosition = self.data_treeWidget.mapToGlobal(QPoint(0, 0))        
        self.dataTreeWidget_QMenu.move(parentPosition + QPos)
        self.dataTreeWidget_QMenu.show() 
        

    def addEntry_pushButton(self):
        data = {"Project A": np.ones((5,1)),
                "Project B": np.zeros((5,1)),
                "Project C": np.ones((5,1))}   
        self.addEntry(data)

    def addEntry(self,data=None):
        items = []
        for key, values in data.items():
            name = key
            desc = "shape=%s dtype=%s" % (values.shape, values.dtype)
            typeStr = type(values).__name__
            item = QTreeWidgetItem([name, typeStr,desc])
            items.append(item)
        self.data_treeWidget.insertTopLevelItems(0, items) 
        [self.data_treeWidget.resizeColumnToContents(col) for col in range(self.data_treeWidget.columnCount())]

    def removeEntry(self,item):
        self.data_treeWidget.takeTopLevelItem(self.data_treeWidget.indexOfTopLevelItem(item))
        # self.data_treeWidget.indexOfTopLevelItem(item)

    def removeEntry_pushButton(self):
        [self.removeEntry(item) for item in self.data_treeWidget.selectedItems()]
        
    def doubleClicked_treeWidget_function(self,item):
        self.showVariable_signal.emit(item.text(0))
        print(item.text(0))

 ################################################## Read Context menu ##########################################    
    def readQMenuSignal(self,input):
        print(input)
        # if input  == 'OpenMBES':
        #     self.getData('MBES','open')
        # elif input  == 'ExtractMBES':
        #     self.getData('MBES','store')            
        # elif input == 'SaveData':
        #     print('Saving data... or not')
        # elif input == 'RemoveItems':
        #     self.removeSelectedItems()
        # elif input == 'ClearList':                        
        #     self.fileSelection_listClearItemClicked()
#     ################################################## Context menu functions ##########################################    

#     def fileSelection_listClearItemClicked(self):
#         [self.removeEntry(item) for item in self.selectAllItems()]
#     def fileSelection_listRemoveItemClicked(self):
#         self.removeSelectedItems()        

#  ################################################## Functions ##########################################    

#     def addEntry(self,item):
#         # Add a new entry to FileSelectionPanel containing item
#         item.setFlags(item.flags() | Qt.ItemIsEditable)
#         self.data_treeWidget.addItem(item)
#         self.data_treeWidget.clearSelection()
#         self.data_treeWidget.setCurrentItem(item)

#     def removeEntry(self,item):
#         self.data_treeWidget.removeChild(self.fileList_Parameters.child(item.text())) # Remove item from parameters
#         self.data_treeWidget.takeItem(self.fileSelection_listWidget.row(item))  # Remove item from list

#     def removeSelectedItems(self):
#         [self.removeEntry(item) for item in self.fileSelection_listWidget.selectedItems()]
        
#     def selectAllItems(self):
#         return [self.fileSelection_listWidget.item(row) for row in range(self.fileSelection_listWidget.count())]

#     def clearAll(self):
#         [self.removeEntry(item) for item in self.selectAllItems()]





def main():
    import numpy as np
    data = {"Project A": np.ones((5,1)),
            "Project B": np.zeros((5,1)),
            "Project C": np.ones((5,1))}    
    import sys
    app = QApplication(['test'])
    tof = CustomDataTreeWidget(data = data)
    tof.show()
    app.exec()

if __name__=="__main__":
    main()


