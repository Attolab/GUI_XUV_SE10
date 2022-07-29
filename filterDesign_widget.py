from re import I
from turtle import Pen
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,SIGNAL,Signal,QItemSelectionModel,Slot,
    QSize, QTime, QUrl, Qt)    
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QAction,QActionGroup,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,QListWidgetItem,QTableWidgetItem,QGridLayout,
    QAbstractItemView,QToolButton,QSizePolicy, QWidget, QFileDialog,QMenu)
from filterDesign_widget_ui import Ui_FilterWidget
from scipy import signal
from convertinator_class import Convertinator as C

class FilterDesignWidget(Ui_FilterWidget,QWidget):
    # toolButtonClicked_signal = Signal(object,object)
    def __init__(self,parent=None):
        super(FilterDesignWidget, self).__init__(parent)
        self.setupUi(self)
        self.connectSignals()
        self.updateGUI()

    def connectSignals(self):
        self.filterRole_comboBox.currentIndexChanged.connect(self.updateGUI)
        self.doPlot_pushButton.pressed.connect(self.computeSpectrum)
        # self.filterType_comboBox.currentIndexChanged.connect(self.updateGUI)
        # self.upperPassBand_doubleSpinBox.valueChanged.connect


    def getFilterType(self):
        filter_type = self.getValue(self.filterType_comboBox)
        if filter_type == 0:   
            filterChoice = 'butter'
        elif filter_type == 1:
            filterChoice = 'cheby1'
        elif filter_type == 2:
            filterChoice = 'cheby2'
        elif filter_type == 3:
            filterChoice = 'ellip'
        elif filter_type == 4:
            filterChoice = 'bessel'   
        return filterChoice
        
    def computeSpectrum(self,**opts):
        filter_role = self.getValue(self.filterRole_comboBox)
        if filter_role == 0:    
            wp = self.getValue(self.lowerPassBand_doubleSpinBox)
            ws = self.getValue(self.lowerStopBand_doubleSpinBox)            
        elif filter_role == 1:
            wp = self.getValue(self.upperPassBand_doubleSpinBox)
            ws = self.getValue(self.upperStopBand_doubleSpinBox)            
        elif filter_role == 2:
            wp = [self.getValue(self.lowerPassBand_doubleSpinBox),self.getValue(self.upperPassBand_doubleSpinBox)]
            ws = [self.getValue(self.upperPassBand_doubleSpinBox),self.getValue(self.upperStopBand_doubleSpinBox)]
        gstop = self.getValue(self.minLossStopBand_doubleSpinBox)
        gpass = self.getValue(self.maxLossPassBand_doubleSpinBox)        
        filterType = self.getFilterType()
        system = signal.iirdesign(wp = wp, ws = ws, gpass = gpass, gstop = gstop,ftype=filterType)


        import matplotlib.pyplot as plt
        import matplotlib.ticker
        import numpy as np
        w, h = signal.freqz(*system)
        fig, ax1 = plt.subplots()
        ax1.set_title('Digital filter frequency response')
        ax1.plot(w, 20 * np.log10(abs(h)), 'b')
        ax1.set_ylabel('Amplitude [dB]', color='b')
        ax1.set_xlabel('Frequency [rad/sample]')
        ax1.grid()
        ax1.set_ylim([-120, 20])
        ax2 = ax1.twinx()
        angles = np.unwrap(np.angle(h))
        ax2.plot(w, angles, 'g')
        ax2.set_ylabel('Angle (radians)', color='g')
        ax2.grid()
        ax2.axis('tight')
        ax2.set_ylim([-6, 1])
        nticks = 8
        ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
        ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
        plt.show()


        signal.filtfilt(*system, np.ones(10))        
    def updateGUI(self):
        filter_role = self.getValue(self.filterRole_comboBox)
        if filter_role == 0:
            self.lowerStopBand_label.setVisible(True)            
            self.lowerPassBand_label.setVisible(True)            
            self.lowerPassBand_doubleSpinBox.setVisible(True)
            self.lowerStopBand_doubleSpinBox.setVisible(True)                
            self.upperStopBand_label.setVisible(False)
            self.upperPassBand_label.setVisible(False)
            self.upperPassBand_doubleSpinBox.setVisible(False)
            self.upperStopBand_doubleSpinBox.setVisible(False)            
        elif filter_role == 1:
            self.lowerStopBand_label.setVisible(False)            
            self.lowerPassBand_label.setVisible(False)            
            self.lowerPassBand_doubleSpinBox.setVisible(False)
            self.lowerStopBand_doubleSpinBox.setVisible(False)        
            self.upperStopBand_label.setVisible(True)
            self.upperPassBand_label.setVisible(True)
            self.upperPassBand_doubleSpinBox.setVisible(True)
            self.upperStopBand_doubleSpinBox.setVisible(True)                                
        elif filter_role == 2:     
            self.lowerStopBand_label.setVisible(True)            
            self.lowerPassBand_label.setVisible(True)            
            self.lowerPassBand_doubleSpinBox.setVisible(True)
            self.lowerStopBand_doubleSpinBox.setVisible(True)                
            self.upperStopBand_label.setVisible(True)
            self.upperPassBand_label.setVisible(True)
            self.upperPassBand_doubleSpinBox.setVisible(True)
            self.upperStopBand_doubleSpinBox.setVisible(True)                      
        elif filter_role == 3:
            self.lowerStopBand_label.setVisible(True)            
            self.lowerPassBand_label.setVisible(True)            
            self.lowerPassBand_doubleSpinBox.setVisible(True)
            self.lowerStopBand_doubleSpinBox.setVisible(True)                
            self.upperStopBand_label.setVisible(True)
            self.upperPassBand_label.setVisible(True)
            self.upperPassBand_doubleSpinBox.setVisible(True)
            self.upperStopBand_doubleSpinBox.setVisible(True)   

    def getValue(self,widget):
        widgetType = widget.__class__.__name__
        # name = widget.objectName()
        if widgetType == 'QComboBox':
            return widget.currentIndex()
        elif widgetType == 'QLineEdit':
            return C.str2float(widget.text())
        elif widgetType == 'QSpinBox':
            return int(widget.value())
        elif widgetType == 'QDoubleSpinBox':
            return float(widget.value())
        elif widgetType == 'QCheckBox':
            return widget.isChecked()                  
        # Set up the user interface from Designer.
    #     self.setupToolButton()
    #     self.setPopupMode(QToolButton.MenuButtonPopup)
    #     self.setToolButtonStyle(Qt.ToolButtonTextOnly)
    #     self.setAutoRaise(True)
    #     self.setArrowType(Qt.RightArrow)        

    # def setupToolButton(self):        
    #     if not self.menu():
    #         self.menu= QMenu(self)       
    #         self.linearRegion_menu = QMenu('Add Linear Region')

    #         self.linearRegionMenu_HorizontalAction = QAction('LR Horizontal')
    #         self.linearRegionMenu_HorizontalAction.setData('LR_H')
    #         self.linearRegionMenu_HorizontalAction.triggered.connect(self.actionClicked)
    #         self.linearRegion_menu.addAction(self.linearRegionMenu_HorizontalAction)

    #         self.linearRegionMenu_VerticalAction = QAction('LR Vertical')
    #         self.linearRegionMenu_VerticalAction.setData('LR_V')
    #         self.linearRegionMenu_VerticalAction.triggered.connect(self.actionClicked)
    #         self.linearRegion_menu.addAction(self.linearRegionMenu_VerticalAction)      

    #         self.infiniteLine_menu = QMenu('Add Infinite Line')

    #         self.infiniteLineMenu_HorizontalAction = QAction('IL Horizontal')
    #         self.infiniteLineMenu_HorizontalAction.setData('IL_H')
    #         self.infiniteLineMenu_HorizontalAction.triggered.connect(self.actionClicked)
    #         self.infiniteLine_menu.addAction(self.infiniteLineMenu_HorizontalAction)

    #         self.infiniteLineMenu_VerticalAction = QAction('IL Vertical')
    #         self.infiniteLineMenu_VerticalAction.setData('IL_V')
    #         self.infiniteLineMenu_VerticalAction.triggered.connect(self.actionClicked)
    #         self.infiniteLine_menu.addAction(self.infiniteLineMenu_VerticalAction)                    

    #         self.menu.addMenu(self.linearRegion_menu)              
    #         self.menu.addMenu(self.infiniteLine_menu)
    #         self.setMenu(self.menu)
    #         self.setDefaultAction(self.infiniteLine_menu.actions()[1])            

    # @Slot(QAction)
    # def actionClicked(self,action):
    #     action = self.sender()
    #     self.toolButtonClicked_signal.emit(self,action)
    #     print(action.text())
    #     print(action.data())  
    #     self.setDefaultAction(action)            


def main():
    import sys
    app = QApplication([])
    tof = FilterDesignWidget()
    tof.show()
    # win =QWidget()
    # layout = QGridLayout()
    # win.setLayout(layout)
    # layout.addWidget(tof)
    # win.show()
    app.exec()

if __name__=="__main__":
    main()
