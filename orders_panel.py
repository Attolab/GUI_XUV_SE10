from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,SIGNAL,QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,QListWidgetItem,
    QSizePolicy, QWidget, QFileDialog,QMenu, QHBoxLayout, QLabel)
from viewer2D_widget import Viewer2DWidget

import numpy as np

class orders_panel(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setupPlots()
        self.setLayout(self.layout)
        #self.doPlot2D(self.AngleViewerWidget, np.array([[1, 0, 0, 1],[1, 1, 0, 0]]))

    def setupPlots(self):
        #self.AlphaViewerWidget = Viewer2DWidget(name = 'Diffraction orders', cmap='magma', labels={'bottom': ('alpha'), 'left': ('pixels') })
        self.AngleViewerWidget = Viewer2DWidget(name = 'Diffraction orders', cmap='magma', labels={'bottom': ('HWP angle'), 'left': ('pixels') })
        self.layout = QHBoxLayout()
        # self.layout.addWidget(QPushButton("Push for Window"))
        #self.layout.addWidget(self.AlphaViewerWidget)
        self.layout.addWidget(self.AngleViewerWidget)


    def doPlot2D(self, item, data, x=None, y=None):
        item.updateViewerWidget(data, x, y)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    W = orders_panel()
    W.show()
    app.exec()
