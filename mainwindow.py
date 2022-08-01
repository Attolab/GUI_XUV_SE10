
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
from fileDetails_tabWidget_ui import Ui_fileDetails_tabwidget
from CustomQMenu import FileSelectionQMenu
import sys, traceback
import h5py
import numpy as np
import os
from pyqtgraph import DataTreeWidget

#for i in *.ui; do pyside6-uic ${i%.ui}.ui > ${i%.ui}_ui.py; done
class MainWindow(QMainWindow,Ui_MainWindow):
    loadData_signal = Signal(object)
    sendData_signal = Signal(object,object)
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)                
        self.setupUi(self)        
        self.setupWindows()
        self.connectSignal()    
        self.path_folder = '' 
        self.workspace = dict() # Create a workspace instance to store data
        self.data = dict() # Temporary array for containing data

    def storeData(self,data_name,data):
        self.data[data_name] = data
    
    def storeDataInWorkspace(self,data_name,data,workspace_name):
        self.workspace[workspace_name] = data
    
    def setupWindows(self):       
        self.fileSelection_dock = QDockWidget('File Selection',self)
        self.fileSelection_widget = FileSelectionPanel()
        self.fileSelection_dock.setWidget(self.fileSelection_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.fileSelection_dock)
        self.mainPanelwidget = MainPanel()
        self.setCentralWidget(self.mainPanelwidget)
        self.showMaximized()

    
    def loadData(self):
        self.path_filenames = QFileDialog.getOpenFileNames(self, 'Choose file',self.path_folder)[0]            
        head_tail = os.path.split(self.path_filenames[0])         
        self.path_folder = head_tail[0]
        self.loadData_signal.emit(self.path_filenames)

    def restore(self):
        self.fileSelection_dock.setFloating(False)
        self.fileSelection_dock.show()

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
        self.loadData_signal.connect(self.fileSelection_widget.storeFiles)

        # CONNECT DATA #
        self.sendData_signal.connect(self.storeData)
        self.sendData_signal.connect(self.storeDataInWorkspace)

        #
        self.fileSelection_widget.sendData_signal.connect(self.mainPanelwidget.showData)

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
