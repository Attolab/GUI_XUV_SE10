
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
        self.fileSelection_tree = ParameterTree()
        self.fileSelection_tree.setHeaderHidden(True)
        self.fileSelection_ParameterTree = Parameter.create(name ='file_list',title='File List',type='group',expandable=True,)
        self.fileSelection_tree.addParameters(self.fileSelection_ParameterTree,showTop=False)
        self.fileSelection_dock2 = QDockWidget('File Selection Dock Widget',self)
        self.fileSelection_dock2.setWidget(self.fileSelection_tree)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.fileSelection_dock2)

        self.fileSelection_dock = QDockWidget('File Selection',self)
        self.fileSelection_widget = FileSelectionPanel()
        self.fileSelection_dock.setWidget(self.fileSelection_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.fileSelection_dock)
        self.mainPanelwidget = MainPanel()
        self.setCentralWidget(self.mainPanelwidget)
        self.showMaximized()

    def transmissionReceived(self):
        print('Got data')

    def loadFile(self):
        print('File loaded') 


    # def press_loadButton_function(self):    
        # self.path_filenames = QFileDialog.getOpenFileNames(self, 'Choose file',self.path_folder)[0]            
        # self.path = self.path_filenames[0]            
        # self.
        # try:
        #     self.loadData(self.path)
        #     [self.addFileToList(filename= path) for path in self.path_filenames if path]
        #     self.fileSelection_listWidget.setCurrentRow(self.fileSelection_listWidget.count())      
        # except:
        #     print('Error loading file') 
    

    def loadData(self):
        self.path_filenames = QFileDialog.getOpenFileNames(self, 'Choose file',self.path_folder)[0]            
        head_tail = os.path.split(self.path_filenames[0])         
        self.path_folder = head_tail[0]
        self.loadData_signal.emit(self.path_filenames)

        # P = Parameter.create(name ='file',title=self.path_filenames[0],type='group',expandable=True,children =)
        
        # [P.addChild(self.storeFile(filename)) for filename in self.path_filenames]
        # Parameter.create(name ='file',title=self.path_filenames[0],type='group',)
        [self.fileSelection_ParameterTree.addChild(self.storeFile(filename)) for filename in self.path_filenames]
        # self.fileSelection_tree.addParameters(Parameter.create(name ='file',title=self.path_filenames[0],type='group',))


    def storeFile(self,filename_fullpath):
        folder,filename_withext = os.path.split(filename_fullpath)
        filename,ext = os.path.splitext(filename_withext)
        size = os.path.getsize(filename_fullpath)
        file_params =  {
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
        return Parameter.create(name=filename, type='group',expanded = False,children = file_params,removable = True,renamable=False)

    def resetGUI_function(self):
        self.close()
        self.__init__()
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
        self.loadData_signal.connect(self.fileSelection_widget.addEntries)

        # CONNECT DATA #
        self.sendData_signal.connect(self.storeData)
        self.sendData_signal.connect(self.storeDataInWorkspace)

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
