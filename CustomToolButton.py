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



class ROIToolButton(QToolButton):
    toolButtonClicked_signal = Signal(object,object)
    def __init__(self,parent=None):
        super(ROIToolButton, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupToolButton()
        self.setPopupMode(QToolButton.MenuButtonPopup)
        self.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.setAutoRaise(True)
        self.setArrowType(Qt.RightArrow)        

    def setupToolButton(self):        
        if not self.menu():
            self.menu= QMenu(self)       
            self.linearRegion_menu = QMenu('Add Linear Region')

            self.linearRegionMenu_HorizontalAction = QAction('LR Horizontal')
            self.linearRegionMenu_HorizontalAction.setData('LR_H')
            self.linearRegionMenu_HorizontalAction.triggered.connect(self.actionClicked)
            self.linearRegion_menu.addAction(self.linearRegionMenu_HorizontalAction)

            self.linearRegionMenu_VerticalAction = QAction('LR Vertical')
            self.linearRegionMenu_VerticalAction.setData('LR_V')
            self.linearRegionMenu_VerticalAction.triggered.connect(self.actionClicked)
            self.linearRegion_menu.addAction(self.linearRegionMenu_VerticalAction)      

            self.infiniteLine_menu = QMenu('Add Infinite Line')

            self.infiniteLineMenu_HorizontalAction = QAction('IL Horizontal')
            self.infiniteLineMenu_HorizontalAction.setData('IL_H')
            self.infiniteLineMenu_HorizontalAction.triggered.connect(self.actionClicked)
            self.infiniteLine_menu.addAction(self.infiniteLineMenu_HorizontalAction)

            self.infiniteLineMenu_VerticalAction = QAction('IL Vertical')
            self.infiniteLineMenu_VerticalAction.setData('IL_V')
            self.infiniteLineMenu_VerticalAction.triggered.connect(self.actionClicked)
            self.infiniteLine_menu.addAction(self.infiniteLineMenu_VerticalAction)                    

            self.menu.addMenu(self.linearRegion_menu)              
            self.menu.addMenu(self.infiniteLine_menu)
            self.setMenu(self.menu)
            self.setDefaultAction(self.infiniteLine_menu.actions()[1])            

    @Slot(QAction)
    def actionClicked(self,action):
        action = self.sender()
        self.toolButtonClicked_signal.emit(self,action)
        print(action.text())
        print(action.data())  
        self.setDefaultAction(action)            


def main():
    import sys
    app = QApplication([])
    tof = ROIToolButton()
    # tof.show()
    win =QWidget()
    layout = QGridLayout()
    win.setLayout(layout)
    layout.addWidget(tof)
    win.show()
    app.exec()

if __name__=="__main__":
    main()
