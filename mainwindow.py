
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
# from panels.DockTitleBar import DockTitleBar
from main_panel import MainPanel
from signal_processing_toolbox import SignalProcessingToolbox
import sys, traceback
import h5py
import numpy as np
#for i in *.ui; do pyside6-uic ${i%.ui}.ui > ${i%.ui}_ui.py; done
class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)                
        self.setupUi(self)        
        self.setupWindows()
        self.connectSignal()    
    def setupWindows(self):       
        # self.fileSelection_dock = QDockWidget('File Selection',self)
        # self.fileSelection_widget = FileSelectionPanel()
        # self.fileSelection_dock.setWidget(self.fileSelection_widget)
        # self.addDockWidget(Qt.LeftDockWidgetArea,self.fileSelection_dock)
        self.mainPanelwidget = MainPanel()
        # self.connectMainPanel()
        self.setCentralWidget(self.mainPanelwidget)


        
    def transmissionReceived(self):
        print('Got data')

    def loadFile(self):
        print('File loaded') 
    def resetGUI_function(self):
        self.close()
        self.__init__()
    def connectSignal(self):
        self.menuFile_restartAction.triggered.connect(restart)
        print('Connecting signal')
        # self._signal_processing_panel = SignalProcessingPanel()
        # self.setCentralWidget(self._signal_processing_panel)


    # def closeEvent(self, event):
        # QMainWindow.closeEvent(event)  

        # QCoreApplication.quit()

        # settings = QSettings("MyCompany", "MyApp")
        # settings.setValue("geometry", saveGeometry())
        # settings.setValue("windowState", saveState())
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
