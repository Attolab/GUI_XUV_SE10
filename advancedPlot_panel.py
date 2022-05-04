##############################################################################
##
# This file is part of pymepixviewer
#
# https://arxiv.org/abs/1905.07999
#
#
# pymepixviewer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pymepixviewer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pymepixviewer.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,
    QSizePolicy, QWidget, QFileDialog,QMenu)
import pyqtgraph as pg
from advancedPlot_panel_ui import Ui_advancedPlot_panel
import numpy as np


class AdvancedPlotPanel(Ui_advancedPlot_panel,QWidget):
    def __init__(self,parent=None,name = 'Viewer1D'):
        super(AdvancedPlotPanel, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # self.connectSignals()
        # self.label = pg.TextItem()


def main():
    import sys
    app = QApplication([])
    tof = AdvancedPlotPanel()
    tof.show()
    app.exec()

if __name__=="__main__":
    main()




    