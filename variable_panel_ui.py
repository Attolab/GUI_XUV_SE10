# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variable_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget)

class Ui_VariablePanel(object):
    def setupUi(self, VariablePanel):
        if not VariablePanel.objectName():
            VariablePanel.setObjectName(u"VariablePanel")
        VariablePanel.resize(450, 274)
        self.gridLayout = QGridLayout(VariablePanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.variablePanel_tabWidget = QTabWidget(VariablePanel)
        self.variablePanel_tabWidget.setObjectName(u"variablePanel_tabWidget")
        self.variablePanel_tabWidget.setTabShape(QTabWidget.Rounded)
        self.variablePanel_tabWidget.setTabsClosable(True)
        self.variablePanel_tabWidget.setMovable(True)

        self.gridLayout.addWidget(self.variablePanel_tabWidget, 0, 0, 1, 1)


        self.retranslateUi(VariablePanel)

        QMetaObject.connectSlotsByName(VariablePanel)
    # setupUi

    def retranslateUi(self, VariablePanel):
        VariablePanel.setWindowTitle(QCoreApplication.translate("VariablePanel", u"Form", None))
    # retranslateUi

