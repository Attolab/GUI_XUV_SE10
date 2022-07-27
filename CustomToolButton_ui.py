# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomToolButton.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_CustomBToolButton(object):
    def setupUi(self, CustomBToolButton):
        if not CustomBToolButton.objectName():
            CustomBToolButton.setObjectName(u"CustomBToolButton")
        CustomBToolButton.resize(172, 42)
        self.actiontest = QAction(CustomBToolButton)
        self.actiontest.setObjectName(u"actiontest")
        self.actiontest.setCheckable(True)
        self.actiontest2 = QAction(CustomBToolButton)
        self.actiontest2.setObjectName(u"actiontest2")
        self.verticalLayout = QVBoxLayout(CustomBToolButton)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.makeROI_toolButton = QToolButton(CustomBToolButton)
        self.makeROI_toolButton.setObjectName(u"makeROI_toolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makeROI_toolButton.sizePolicy().hasHeightForWidth())
        self.makeROI_toolButton.setSizePolicy(sizePolicy)
        self.makeROI_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.makeROI_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.makeROI_toolButton.setAutoRaise(True)
        self.makeROI_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.makeROI_toolButton)


        self.retranslateUi(CustomBToolButton)

        QMetaObject.connectSlotsByName(CustomBToolButton)
    # setupUi

    def retranslateUi(self, CustomBToolButton):
        CustomBToolButton.setWindowTitle(QCoreApplication.translate("CustomBToolButton", u"Form", None))
        self.actiontest.setText(QCoreApplication.translate("CustomBToolButton", u"test", None))
        self.actiontest2.setText(QCoreApplication.translate("CustomBToolButton", u"test2", None))
        self.makeROI_toolButton.setText(QCoreApplication.translate("CustomBToolButton", u"Tool Button", None))
    # retranslateUi

