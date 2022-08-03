
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

class FileSelectionQMenu(QMenu):
    removeItem_signal = Signal()
    clearTable_signal = Signal()    
    QActionOperation_signal = Signal(str)
    def __init__(self,parent=None,selection=None):
        super(FileSelectionQMenu, self).__init__(parent)
        
        self.data_menu = QMenu("Data",self)        
        self.addMenu(self.data_menu)

        self.openData_menu = QMenu("Open with ...",self)        
        self.openDataMBESE_action = QAction("MBES...",self.openData_menu)
        self.data_menu.addMenu(self.openData_menu)

        self.extractData_menu = QMenu("Extract as ...",self)        
        self.extractDataMBESE_action = QAction("MBES...",self.extractData_menu)
        self.data_menu.addMenu(self.extractData_menu)
        self.addSeparator()




        self.extractData_menu.addAction(self.extractDataMBESE_action)
        self.extractData_menu.addSeparator()
        self.saveData_action = QAction("Save Data",self)
        self.removeItem_action = QAction("Remove Item(s)",self)
        self.clearTable_action = QAction("Clear all",self)

        self.addAction(self.saveData_action)
        self.addAction(self.removeItem_action)
        self.addAction(self.clearTable_action)      
        self.openDataMBESE_action.setData('OpenMBES')
        self.extractDataMBESE_action.setData('ExtractMBES')
        self.saveData_action.setData('SaveData')
        self.removeItem_action.setData('RemoveItems')
        self.clearTable_action.setData('ClearList')

        self.openDataMBESE_action.triggered.connect(self.QAction_function)
        self.extractDataMBESE_action.triggered.connect(self.QAction_function)
        self.saveData_action.triggered.connect(self.QAction_function)
        self.removeItem_action.triggered.connect(self.QAction_function)
        self.clearTable_action.triggered.connect(self.QAction_function)
        self.updateSelection(selection)

    def updateSelection(self,selection = None):
        status = bool(selection)
        self.data_menu.setEnabled(status)
        self.removeItem_action.setEnabled(status)

    def QAction_function(self,):
        self.QActionOperation_signal.emit(self.sender().data())    
        # self.data_menu.addMenu(self.extractData_menu)
        # self.extractAllData_menu = QMenu("Extract all",self)
        # self.data_menu.addMenu(self.extractData_menu)
        # self.extractAllData_menu.addSeparator()
        # self.extractData_GlobalWorkspace_action = QAction("in global workspace",self)
        # self.extractData_NewWorkspace_action = QAction("in new workspace",self)
        # self.extractData_ExistingWorkSpace_menu = QMenu("in workspace ...",self) #         
        # # ADD ACTION FOR EACH EXISTING WORKSPACE
        # self.extractData_menu.addAction(self.extractData_GlobalWorkspace_action)  
        # self.extractData_menu.addAction(self.extractData_NewWorkspace_action)        
        # self.extractData_menu.addMenu(self.extractData_ExistingWorkSpace_menu)        


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