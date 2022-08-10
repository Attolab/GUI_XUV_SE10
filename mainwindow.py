
from ast import Param
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal,QProcess)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QWindow,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QWidget,QDockWidget,QFileDialog,QTableWidgetItem,QHBoxLayout)
import pyqtgraph as pg
from mainwindow_ui import Ui_MainWindow
from fileSelection_panel import FileSelectionPanel
# from panels.DockTitleBar import DockTitleBar
from main_panel import MainPanel
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
from pyqtgraph.parametertree import Parameter
from pyqtgraph.parametertree import ParameterTree
from signal_processing_toolbox import SignalProcessingToolbox
from CustomQMenu import FileSelectionQMenu
import sys, traceback
import h5py
import numpy as np
import os
from CustomDataTreeWidget import CustomDataTreeWidget
from pyqtgraph import DataTreeWidget

#for i in *.ui; do pyside6-uic ${i%.ui}.ui > ${i%.ui}_ui.py; done
class MainWindow(QMainWindow,Ui_MainWindow):
    loadData_signal = Signal(object)
    sendData_signal = Signal(object)
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)                
        self.setupUi(self)          
        self.path_folder = '' 
        self._workspace = dict() # Create a workspace instance to store data
        self._data = dict() # Temporary array for containing data
        self._dock = dict()
        self._widgets = dict()
        self.setupWindows()
        self.connectSignal()          

    def storeData(self,data):
        self.extractDictEntry(data.value())
        self.sendData_signal.emit(self._data)


    def extractDictEntry(self,entry):
        for key,value in entry.items():
            if type(value) is dict:
                self.extractDictEntry(value)
            else:
                self._data[key] = value



    def storeDataInWorkspace(self,data_name,data,workspace_name):
        self._workspace[workspace_name] = data
    
    def setupWindows(self):       
        dock = QDockWidget('File Selection',self)
        widget = FileSelectionPanel()
        dock.setWidget(widget)
        self.addDockWidget(Qt.LeftDockWidgetArea,dock)
        self._dock['fileSelection_dock'] = dock
        self._widgets['fileSelection_widget'] = widget        
        self.openMBES()
        self.showMaximized() 

        dock = QDockWidget('Data Browser',self)
        widget = CustomDataTreeWidget()
        dock.setWidget(widget)
        self.addDockWidget(Qt.BottomDockWidgetArea,dock)
        self._dock['dataBrowser_dock'] = dock
        self._widgets['dataBrowser_widget'] = widget        


    def openMBES(self):
        dock = QDockWidget('MBES Panel',self,floating=False)
        widget = MainPanel()        
        dock.setWidget(widget)
        self.addDockWidget(Qt.RightDockWidgetArea,dock)
        self._dock['MBES_dock'] = dock        
        self._widgets['MBES_widget'] = widget
    
    def loadData(self):
        self.path_filenames = QFileDialog.getOpenFileNames(self, 'Choose file',self.path_folder)[0]            
        head_tail = os.path.split(self.path_filenames[0])         
        self.path_folder = head_tail[0]
        self.loadData_signal.emit(self.path_filenames)

    def restore(self):
        for dock in self._dock.values():
            dock.setFloating(False)
            dock.show()

    def connectSignal(self):
        # CONNECT ACTIONS #
        self.restart_action.triggered.connect(restart)
        self.restart_action.setShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_Q))
        self.quit_action.triggered.connect(self.close)
        self.quit_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q))

        self.load_action.triggered.connect(self.loadData)
        self.load_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_L))

        self.restoreState_action.triggered.connect(self.restore)
        self.restoreState_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_R))

        # CONNECT FILE SELECTION PANEL #
        self.loadData_signal.connect(self._widgets['fileSelection_widget'].storeFiles)

        # CONNECT DATA #
        # self._widgets['fileSelection_widget'].sendData_signal.connect(self._widgets['dataBrowser_widget'].addEntry)
        # self.sendData_signal.connect(self.storeDataInWorkspace)
        # self.sendData_signal.connect(self._widgets['dataBrowser_widget'].addData)
        self._widgets['fileSelection_widget'].sendData_signal.connect(self._widgets['dataBrowser_widget'].storeData)

        #
        # self._widgets['fileSelection_widget'].sendData_signal.connect(self._widgets['MBES_widget'].showData)

        print('Connecting signal')

    def quit(self):
        self.close()
def restart():
    QCoreApplication.quit()
    status = QProcess.startDetached(sys.executable, sys.argv)
    print(f'Exiting status: {status}')
        #  
def main():
    import sys
    app = QApplication([])
    tools = MainWindow()
    tools.show()
    app.exec()
if __name__=="__main__":
    main()
