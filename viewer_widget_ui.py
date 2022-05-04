# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_ViewerWidget(object):
    def setupUi(self, ViewerWidget):
        if not ViewerWidget.objectName():
            ViewerWidget.setObjectName(u"ViewerWidget")
        ViewerWidget.resize(788, 314)
        self.horizontalLayout = QHBoxLayout(ViewerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.viewer_GraphicsLayoutWidget = GraphicsLayoutWidget(ViewerWidget)
        self.viewer_GraphicsLayoutWidget.setObjectName(u"viewer_GraphicsLayoutWidget")

        self.horizontalLayout.addWidget(self.viewer_GraphicsLayoutWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.show2D_checkBox = QCheckBox(ViewerWidget)
        self.show2D_checkBox.setObjectName(u"show2D_checkBox")
        self.show2D_checkBox.setChecked(True)
        self.show2D_checkBox.setTristate(False)

        self.verticalLayout.addWidget(self.show2D_checkBox)

        self.showHist_checkBox = QCheckBox(ViewerWidget)
        self.showHist_checkBox.setObjectName(u"showHist_checkBox")
        self.showHist_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.showHist_checkBox)

        self.showSum_checkBox = QCheckBox(ViewerWidget)
        self.showSum_checkBox.setObjectName(u"showSum_checkBox")

        self.verticalLayout.addWidget(self.showSum_checkBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ViewerWidget)

        QMetaObject.connectSlotsByName(ViewerWidget)
    # setupUi

    def retranslateUi(self, ViewerWidget):
        ViewerWidget.setWindowTitle(QCoreApplication.translate("ViewerWidget", u"Form", None))
        self.show2D_checkBox.setText(QCoreApplication.translate("ViewerWidget", u"Show 2D", None))
        self.showHist_checkBox.setText(QCoreApplication.translate("ViewerWidget", u"Show Hist", None))
        self.showSum_checkBox.setText(QCoreApplication.translate("ViewerWidget", u"Show Sum", None))
    # retranslateUi

