from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal,QProcess)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar, QDialog,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)
from variable_panel_ui import Ui_VariablePanel
from variable_item_ui import Ui_VariableItem



class VariablePanel(Ui_VariablePanel,QWidget):
    signal_closetab = Signal(int)
    def __init__(self,parent=None,name='TestPanel'):
        super(VariablePanel, self).__init__(parent)                
        self.setupUi(self)     
        self.setObjectName(name)
        self.name = name
        self.connectSignals()

    def get_TabPanelWidget(self):
        return self.variablePanel_tabWidget

    def get_numberofTabs(self):
        return self.variablePanel_tabWidget.count()

    def insertTab(self,widget,name:str,index:int):
        self.variablePanel_tabWidget.insertTab(index,widget,name)

    def getTabIndexfromWidget(self,item):
        return self.variablePanel_tabWidget.indexOf(item)

    def setTab(self,item):
        self.variablePanel_tabWidget.setCurrentIndex(self.getTabIndexfromWidget(item))

    def connectSignals(self):    
        self.variablePanel_tabWidget.tabCloseRequested.connect(self.closeTab_function)  

    def closeTab_fromWidget_function(self,item):
        self.closeTab_function(self.getTabIndexfromWidget(item))

    def closeTab_function(self,index):
        self.signal_closetab.emit(index)
        self.variablePanel_tabWidget.removeTab(index)    

    def setTab_fromWidget_function(self,item):
        widget = item.get_widgetDataVariableItem()
        if self.getTabIndexfromWidget(widget) == -1:
            self.insertTab(widget,item.text(),self.get_numberofTabs())
        self.setTab(widget) 
        self.showTab()

    def showTab(self):
        if not(self.isVisible()):
            self.show()
        self.activateWindow()        

class VariableItemTable(Ui_VariableItem,QWidget):

    def __init__(self,parent=None,name = 'TestItem',input = None):
        super(VariableItemTable, self).__init__(parent)                
        self.setupUi(self) 
        self.setObjectName(name)
        self.name = name    
        self.connectSignals()

    def connectSignals(self):
        self.variable_tableWidget.itemDoubleClicked.connect(self.doubleClicked)  

    def doubleClicked(self,doubleClickedIndex):
        rowindex = doubleClickedIndex.row()
        colindex = doubleClickedIndex.column()
        print(f'Double clicked: ({rowindex},{colindex})')
        
    def get_numberofRows(self):
        return self.variable_tableWidget.rowCount()

    def get_numberofCols(self):
        return self.variable_tableWidget.columnCount()

    def set_numberofCols(self, input:int):
        return self.variable_tableWidget.setColumnCount(input)        

    def set_numberofRows(self, input:int):
        return self.variable_tableWidget.setRowCount(input)

    def set_item(self, row_index:int, col_index:int, value):
        if isinstance(value,str):
            self.variable_tableWidget.setItem(row_index,col_index,QTableWidgetItem(value))
        else:
            self.variable_tableWidget.setItem(row_index,col_index,QTableWidgetItem(str(value)))

    def getTabIndexfromWidget(self ,item:QTableWidgetItem):
        return self.variable_tableWidget.indexFromItem(item)

    def get_TableWidget(self):
        return self.variable_tableWidget
# ''' The object that popups when double-clicking on a "environment" variable'''

# class varDialog(QDialog):
#     def __init__(self, index):
#         super(varDialog, self).__init__(parent)

#         self.varname = cts.varlist[index][0]
#         self.var = cts.varlist[index][1]
#         self.par = self.parent()

#         self.setGeometry(850, 500, 450, 300)
#         self.setWindowTitle(self.varname)
#         self.mainlayout = QHBoxLayout()

#         self.table = QTableWidget()
#         self.table.setSelectionBehavior(QTableView.SelectRows)

#         if(isinstance(self.var, int) or isinstance(self.var, float)):
#             self.table.setColumnCount(1)
#             self.table.setRowCount(1)
#             self.table.setItem(0, 0, QTableWidgetItem(str(self.var)))

#         if isinstance(self.var, str):
#             self.table.setColumnCount(1)
#             self.table.setRowCount(1)
#             self.table.setItem(0, 0, QTableWidgetItem(self.var))

#         if(isinstance(self.var, np.ndarray)):
#             rownb = self.var.shape[0]
#             try:
#                 colnb = self.var.shape[1]
#             except IndexError:
#                 colnb = 1
#             self.table.setColumnCount(colnb)
#             self.table.setRowCount(rownb)

#             for i in range(rownb):
#                 if colnb == 1:
#                     self.table.setItem(i, 0, QTableWidgetItem("{:.3e}".format(self.var[i])))
#                 else:
#                     for j in range(colnb):
#                         self.table.setItem(i, j, QTableWidgetItem("{:.3e}".format(self.var[i,j])))


#         self.mainlayout.addWidget(self.table)
#         self.setLayout(self.mainlayout)
#         self.show()
def main():
    app = QApplication([])
    widget = VariablePanel()
    widget.show()
    widget_item = VariableItemTable(name = '0')
    widget.variablePanel_tabWidget.insertTab(0,widget_item,'0')  
    widget_item2 = VariableItemTable(name = '1')
  
    widget.variablePanel_tabWidget.insertTab(1,widget_item2,'1')   
    widget_item3 = VariableItemTable(name = '1')
  
    widget.variablePanel_tabWidget.insertTab(2,widget_item3,'2')       
    widget_item = QTableWidgetItem('0')

    widget_item = VariableItemTable(name = '0')
    widget.variablePanel_tabWidget.insertTab(0,widget_item,'0')  
    widget_item2 = VariableItemTable(name = '1')
  
    widget.variablePanel_tabWidget.insertTab(1,widget_item2,'1')   
    widget_item3 = VariableItemTable(name = '1')
  
    widget.variablePanel_tabWidget.insertTab(2,widget_item3,'2')       
    widget_item = QTableWidgetItem('0')

    app.exec()
if __name__=="__main__":
    main()
