# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advancedPlot_toolbox.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QToolBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(792, 570)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(595, 260, 141, 101))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 230, 91, 25))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(630, 130, 92, 23))
        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(630, 170, 92, 23))
        self.toolBox = QToolBox(Form)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(110, 50, 301, 251))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 301, 189))
        self.comboBox = QComboBox(self.page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 10, 86, 25))
        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 301, 189))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.retranslateUi(Form)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add ROI", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Hist", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Sum", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1D", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"2D", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"3D", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Form", u"Page 2", None))
    # retranslateUi

