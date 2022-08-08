
from encodings import normalize_encoding
from pyqtgraph import TableWidget

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,SIGNAL,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QPushButton, QSizePolicy, QToolButton,QMenu,QTableWidget,QCheckBox,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow,QHeaderView)
import numpy as np

import pyqtgraph as pg



class baseQMenu(QMenu):
    QActionOperation_signal = Signal(str)
    def __init__(self,parent=None):
        super(baseQMenu, self).__init__(parent)
        self.removeItem_action = QAction("Remove Item(s)",self)
        self.removeItem_action.setData('removeItems')
        self.clearTable_action = QAction("Clear all",self)
        self.clearTable_action.setData('clearList')
        self.addAction(self.removeItem_action)
        self.addAction(self.clearTable_action) 

        self.removeItem_action.triggered.connect(self.QAction_function)
        self.clearTable_action.triggered.connect(self.QAction_function)   

    def QAction_function(self,):
        self.QActionOperation_signal.emit(self.sender().data())    

class FileSelectionQMenu(baseQMenu):
    QActionOperation_signal = Signal(str)
    def __init__(self,parent=None,selection=None):
        super(FileSelectionQMenu, self).__init__(parent)
        
        self.addSeparator()
        self.data_menu = QMenu("Data",self)        

        self.openData_menu = QMenu("Open with ...",self)        
        self.openDataMBESE_action = QAction("MBES...",self.openData_menu)
        self.openDataMBESE_action.setData('openMBES')
        self.data_menu.addMenu(self.openData_menu)

        self.extractData_menu = QMenu("Extract as ...",self)        
        self.extractDataMBESE_action = QAction("MBES...",self.extractData_menu)
        self.extractDataMBESE_action.setData('extractMBES')
        self.extractData_menu.addAction(self.extractDataMBESE_action)
        self.data_menu.addMenu(self.extractData_menu)

        self.insertMenu(self.removeItem_action,self.data_menu)        

        self.saveData_action = QAction("Save Data",self)
        self.saveData_action.setData('saveData')
        
        self.addAction(self.saveData_action)
    
        self.openDataMBESE_action.triggered.connect(self.QAction_function)
        self.extractDataMBESE_action.triggered.connect(self.QAction_function)
        self.saveData_action.triggered.connect(self.QAction_function)
        self.updateSelection(selection)

    def updateSelection(self,selection = None):
        status = bool(selection)
        self.data_menu.setEnabled(status)
        self.removeItem_action.setEnabled(status)


class DataSelectionQMenu(baseQMenu):
    QActionOperation_signal = Signal(str)
    def __init__(self,parent=None,selection=None):
        super(DataSelectionQMenu, self).__init__(parent)
        
        self.copyData_action = QAction("Copy",self)
        self.copyData_action.setData('copy')
        self.copyData_action.triggered.connect(self.QAction_function)

        self.insertAction(self.removeItem_action,self.copyData_action)        
        self.insertSeparator(self.removeItem_action)

        self.operation_menu = QMenu('Operation',self)
        self.sumData_menu = QMenu('Sum',self.operation_menu)
        self.substractData_menu = QMenu('Substract',self.operation_menu)
        self.normalizeData_menu = QMenu('Normalize',self.operation_menu)

        self.sumData2_action = QAction('along axis 2',self.sumData_menu)
        self.sumData2_action.setData('sum2')        
        self.sumData1_action = QAction('along axis 1',self.sumData_menu)
        self.sumData1_action.setData('sum1')        
        self.sumData0_action = QAction('along all axis',self.sumData_menu)
        self.sumData0_action.setData('sum0')
        self.sumData_menu.addAction(self.sumData0_action)
        self.sumData_menu.addAction(self.sumData1_action)
        self.sumData_menu.addAction(self.sumData2_action)

        self.substractData_menu = QMenu('Substract',self.operation_menu)
        self.substractData2_action = QAction('along axis 2',self.sumData_menu)
        self.sumData2_action.setData('sum2')        
        self.sumData1_action = QAction('along axis 1',self.sumData_menu)
        self.sumData1_action.setData('sum1')        
        self.sumData0_action = QAction('along all axis',self.sumData_menu)
        self.sumData0_action.setData('sum0')
        self.sumData_menu.addAction(self.sumData0_action)
        self.sumData_menu.addAction(self.sumData1_action)
        self.sumData_menu.addAction(self.sumData2_action)


        self.normalizeData_menu = QMenu('Normalize',self.operation_menu)
        self.normalizeData2_action = QAction('along axis 2',self.normalizeData_menu)
        self.normalizeData2_action.setData('normalize2')        
        self.normalizeData1_action = QAction('along axis 1',self.normalizeData_menu)
        self.normalizeData1_action.setData('normalize1')        
        self.normalizeData0_action = QAction('along all axis',self.normalizeData_menu)
        self.normalizeData0_action.setData('normalize0')
        self.normalizeData_menu.addAction(self.normalizeData0_action)
        self.normalizeData_menu.addAction(self.normalizeData1_action)
        self.normalizeData_menu.addAction(self.normalizeData2_action)



        self.operation_menu.addMenu(self.sumData_menu)
        self.operation_menu.addMenu(self.normalizeData_menu)
        self.insertMenu(self.copyData_action,self.operation_menu)
        self.insertSeparator(self.copyData_action)

    def updateSelection(self,selection = None):
        status = bool(selection)
        self.removeItem_action.setEnabled(status)        





class CustomQMenu(QMenu):
    removeItem_signal = Signal()
    clearTable_signal = Signal()
    def __init__(self,parent=None):
        super(CustomQMenu, self).__init__(parent)
        self.removeItem_action = QAction("Remove Item(s)",self)
        self.removeItem_action.triggered.connect(self.removeItem_signal.emit)

        self.clearTable_action = QAction("Clear all",self)
        self.clearTable_action.triggered.connect(self.clearTable_signal.emit)

        self.addAction(self.removeItem_action)
        self.addAction(self.clearTable_action)        


class functionOperationQMenu(QMenu):
    findPeak_signal = Signal()
    doFFT_signal = Signal()
    def __init__(self,parent=None):
        super(CustomQMenu, self).__init__(parent)
        self.findPeak_action = QAction("Find Peak(s)",self)
        self.findPeak_action.triggered.connect(self.findPeak_signal.emit)

        self.doFFT_action = QAction("FFT",self)
        self.doFFT_action.triggered.connect(self.doFFT_signal.emit)

        self.addAction(self.doFFT_action)
        self.addAction(self.findPeak_action)     



class ROIOperationQMenu(QMenu):
    QActionOperation_signal = Signal(str)
    def __init__(self,parent=None):
        super(ROIOperationQMenu, self).__init__(parent)

        self.COM_action = QAction("COM",self)
        self.sum_action = QAction("Sum",self)
        self.findMax_action = QAction("Max",self)
        self.findMin_action = QAction("Min",self)

        self.COM_action.setData('COM')
        self.sum_action.setData('Sum')
        self.findMax_action.setData('Max')
        self.findMin_action.setData('Min')

        self.COM_action.triggered.connect(self.QAction_function)
        self.sum_action.triggered.connect(self.QAction_function)
        self.findMax_action.triggered.connect(self.QAction_function)
        self.findMin_action.triggered.connect(self.QAction_function)

        self.addAction(self.COM_action)
        self.addAction(self.sum_action)
        self.addAction(self.findMax_action)
        self.addAction(self.findMin_action)      


    def QAction_function(self):
        self.QActionOperation_signal.emit(self.sender().data())    