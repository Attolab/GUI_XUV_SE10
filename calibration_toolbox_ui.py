# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_toolbox.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_CalibrationToolbox(object):
    def setupUi(self, CalibrationToolbox):
        if not CalibrationToolbox.objectName():
            CalibrationToolbox.setObjectName(u"CalibrationToolbox")
        CalibrationToolbox.resize(853, 520)
        self.horizontalLayout_5 = QHBoxLayout(CalibrationToolbox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.loadSignal_toolButton = QToolButton(CalibrationToolbox)
        self.loadSignal_toolButton.setObjectName(u"loadSignal_toolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadSignal_toolButton.sizePolicy().hasHeightForWidth())
        self.loadSignal_toolButton.setSizePolicy(sizePolicy)
        self.loadSignal_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.loadSignal_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.loadSignal_toolButton.setAutoRaise(False)
        self.loadSignal_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.loadSignal_toolButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.findPeaks_toolButton = QToolButton(CalibrationToolbox)
        self.findPeaks_toolButton.setObjectName(u"findPeaks_toolButton")
        sizePolicy.setHeightForWidth(self.findPeaks_toolButton.sizePolicy().hasHeightForWidth())
        self.findPeaks_toolButton.setSizePolicy(sizePolicy)
        self.findPeaks_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.findPeaks_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.findPeaks_toolButton.setAutoRaise(False)
        self.findPeaks_toolButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.findPeaks_toolButton)

        self.toolButton = QToolButton(CalibrationToolbox)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.findPeaks_comboBox = QComboBox(CalibrationToolbox)
        self.findPeaks_comboBox.setObjectName(u"findPeaks_comboBox")
        self.findPeaks_comboBox.setEnabled(False)

        self.verticalLayout.addWidget(self.findPeaks_comboBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.autoFillTable_checkBox = QCheckBox(CalibrationToolbox)
        self.autoFillTable_checkBox.setObjectName(u"autoFillTable_checkBox")
        self.autoFillTable_checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.autoFillTable_checkBox)

        self.considerSBs_checkBox = QCheckBox(CalibrationToolbox)
        self.considerSBs_checkBox.setObjectName(u"considerSBs_checkBox")
        self.considerSBs_checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.considerSBs_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(CalibrationToolbox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.centraFrequency_doubleSpinBox = QDoubleSpinBox(CalibrationToolbox)
        self.centraFrequency_doubleSpinBox.setObjectName(u"centraFrequency_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.centraFrequency_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.centraFrequency_doubleSpinBox.setSizePolicy(sizePolicy)
        self.centraFrequency_doubleSpinBox.setKeyboardTracking(False)
        self.centraFrequency_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.centraFrequency_doubleSpinBox.setMaximum(10000000.000000000000000)
        self.centraFrequency_doubleSpinBox.setValue(800.000000000000000)

        self.horizontalLayout_4.addWidget(self.centraFrequency_doubleSpinBox)

        self.label_4 = QLabel(CalibrationToolbox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.listPeaks_tableWidget = QTableWidget(CalibrationToolbox)
        if (self.listPeaks_tableWidget.columnCount() < 2):
            self.listPeaks_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.listPeaks_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.listPeaks_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.listPeaks_tableWidget.setObjectName(u"listPeaks_tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listPeaks_tableWidget.sizePolicy().hasHeightForWidth())
        self.listPeaks_tableWidget.setSizePolicy(sizePolicy2)
        self.listPeaks_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listPeaks_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.listPeaks_tableWidget)

        self.showPeaks_checkBox = QCheckBox(CalibrationToolbox)
        self.showPeaks_checkBox.setObjectName(u"showPeaks_checkBox")

        self.verticalLayout.addWidget(self.showPeaks_checkBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fitPeaks_pushButton = QPushButton(CalibrationToolbox)
        self.fitPeaks_pushButton.setObjectName(u"fitPeaks_pushButton")

        self.horizontalLayout.addWidget(self.fitPeaks_pushButton)

        self.label = QLabel(CalibrationToolbox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.calibration_toolButton = QToolButton(CalibrationToolbox)
        self.calibration_toolButton.setObjectName(u"calibration_toolButton")
        sizePolicy.setHeightForWidth(self.calibration_toolButton.sizePolicy().hasHeightForWidth())
        self.calibration_toolButton.setSizePolicy(sizePolicy)
        self.calibration_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.calibration_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.calibration_toolButton.setAutoRaise(False)
        self.calibration_toolButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.calibration_toolButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.coeffCalib_tableWidget = QTableWidget(CalibrationToolbox)
        if (self.coeffCalib_tableWidget.columnCount() < 3):
            self.coeffCalib_tableWidget.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.coeffCalib_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.coeffCalib_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.coeffCalib_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.coeffCalib_tableWidget.setObjectName(u"coeffCalib_tableWidget")
        sizePolicy2.setHeightForWidth(self.coeffCalib_tableWidget.sizePolicy().hasHeightForWidth())
        self.coeffCalib_tableWidget.setSizePolicy(sizePolicy2)
        self.coeffCalib_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.coeffCalib_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.coeffCalib_tableWidget)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plotRaw_window = GraphicsLayoutWidget(CalibrationToolbox)
        self.plotRaw_window.setObjectName(u"plotRaw_window")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plotRaw_window.sizePolicy().hasHeightForWidth())
        self.plotRaw_window.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.plotRaw_window)

        self.plotCalib_window = GraphicsLayoutWidget(CalibrationToolbox)
        self.plotCalib_window.setObjectName(u"plotCalib_window")
        sizePolicy3.setHeightForWidth(self.plotCalib_window.sizePolicy().hasHeightForWidth())
        self.plotCalib_window.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.plotCalib_window)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.retranslateUi(CalibrationToolbox)

        QMetaObject.connectSlotsByName(CalibrationToolbox)
    # setupUi

    def retranslateUi(self, CalibrationToolbox):
        CalibrationToolbox.setWindowTitle(QCoreApplication.translate("CalibrationToolbox", u"Form", None))
        self.loadSignal_toolButton.setText(QCoreApplication.translate("CalibrationToolbox", u"Find Peaks", None))
        self.findPeaks_toolButton.setText(QCoreApplication.translate("CalibrationToolbox", u"Fit data", None))
        self.toolButton.setText(QCoreApplication.translate("CalibrationToolbox", u"...", None))
        self.autoFillTable_checkBox.setText(QCoreApplication.translate("CalibrationToolbox", u"AutoFill", None))
        self.considerSBs_checkBox.setText(QCoreApplication.translate("CalibrationToolbox", u"With Sidebands", None))
        self.label_5.setText(QCoreApplication.translate("CalibrationToolbox", u"Central frequency", None))
        self.centraFrequency_doubleSpinBox.setPrefix("")
        self.centraFrequency_doubleSpinBox.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("CalibrationToolbox", u"nm", None))
        ___qtablewidgetitem = self.listPeaks_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CalibrationToolbox", u"Time", None));
        ___qtablewidgetitem1 = self.listPeaks_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CalibrationToolbox", u"Energy", None));
        self.showPeaks_checkBox.setText(QCoreApplication.translate("CalibrationToolbox", u"Show Peaks", None))
        self.fitPeaks_pushButton.setText(QCoreApplication.translate("CalibrationToolbox", u"Fit Peaks", None))
        self.label.setText(QCoreApplication.translate("CalibrationToolbox", u"Expression: A / t^2 + B", None))
        self.calibration_toolButton.setText(QCoreApplication.translate("CalibrationToolbox", u"Apply Calibration", None))
        ___qtablewidgetitem2 = self.coeffCalib_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CalibrationToolbox", u"A", None));
        ___qtablewidgetitem3 = self.coeffCalib_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CalibrationToolbox", u"B", None));
        ___qtablewidgetitem4 = self.coeffCalib_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CalibrationToolbox", u"t0", None));
    # retranslateUi

