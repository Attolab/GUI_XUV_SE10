# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'variable_item.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_VariableItem(object):
    def setupUi(self, VariableItem):
        if not VariableItem.objectName():
            VariableItem.setObjectName(u"VariableItem")
        VariableItem.resize(427, 259)
        self.gridLayout = QGridLayout(VariableItem)
        self.gridLayout.setObjectName(u"gridLayout")
        self.variable_tableWidget = QTableWidget(VariableItem)
        if (self.variable_tableWidget.columnCount() < 4):
            self.variable_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.variable_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.variable_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.variable_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.variable_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.variable_tableWidget.setObjectName(u"variable_tableWidget")
        self.variable_tableWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.variable_tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.variable_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.variable_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.variable_tableWidget, 0, 0, 1, 1)


        self.retranslateUi(VariableItem)

        QMetaObject.connectSlotsByName(VariableItem)
    # setupUi

    def retranslateUi(self, VariableItem):
        VariableItem.setWindowTitle(QCoreApplication.translate("VariableItem", u"Form", None))
        ___qtablewidgetitem = self.variable_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VariableItem", u"name", None));
        ___qtablewidgetitem1 = self.variable_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VariableItem", u"shape", None));
        ___qtablewidgetitem2 = self.variable_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VariableItem", u"dtype", None));
        ___qtablewidgetitem3 = self.variable_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VariableItem", u"value", None));
    # retranslateUi

