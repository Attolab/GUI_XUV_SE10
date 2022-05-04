# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_panel.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_main_panel(object):
    def setupUi(self, main_panel):
        if not main_panel.objectName():
            main_panel.setObjectName(u"main_panel")
        main_panel.resize(760, 669)
        self.horizontalLayout_6 = QHBoxLayout(main_panel)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.h_centralLayout = QHBoxLayout()
        self.h_centralLayout.setObjectName(u"h_centralLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.h_centralLayout.addItem(self.horizontalSpacer)

        self.v_optionLayout = QVBoxLayout()
        self.v_optionLayout.setObjectName(u"v_optionLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(main_panel)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.folderBase_lineEdit = QLineEdit(main_panel)
        self.folderBase_lineEdit.setObjectName(u"folderBase_lineEdit")

        self.horizontalLayout_3.addWidget(self.folderBase_lineEdit)

        self.forderSelection_toolButton = QToolButton(main_panel)
        self.forderSelection_toolButton.setObjectName(u"forderSelection_toolButton")

        self.horizontalLayout_3.addWidget(self.forderSelection_toolButton)


        self.v_optionLayout.addLayout(self.horizontalLayout_3)

        self.loadSpectrum_pushButton = QPushButton(main_panel)
        self.loadSpectrum_pushButton.setObjectName(u"loadSpectrum_pushButton")

        self.v_optionLayout.addWidget(self.loadSpectrum_pushButton)

        self.fileSelection_listWidget = QListWidget(main_panel)
        self.fileSelection_listWidget.setObjectName(u"fileSelection_listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileSelection_listWidget.sizePolicy().hasHeightForWidth())
        self.fileSelection_listWidget.setSizePolicy(sizePolicy)
        self.fileSelection_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.v_optionLayout.addWidget(self.fileSelection_listWidget)

        self.groupBox = QGroupBox(main_panel)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.makeCalibration_pushButton = QPushButton(self.groupBox)
        self.makeCalibration_pushButton.setObjectName(u"makeCalibration_pushButton")

        self.horizontalLayout_2.addWidget(self.makeCalibration_pushButton)

        self.loadCalibration_pushButton = QPushButton(self.groupBox)
        self.loadCalibration_pushButton.setObjectName(u"loadCalibration_pushButton")

        self.horizontalLayout_2.addWidget(self.loadCalibration_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.alphaCalib_label = QLabel(self.groupBox)
        self.alphaCalib_label.setObjectName(u"alphaCalib_label")

        self.gridLayout.addWidget(self.alphaCalib_label, 1, 0, 1, 1)

        self.betaCalib_label = QLabel(self.groupBox)
        self.betaCalib_label.setObjectName(u"betaCalib_label")

        self.gridLayout.addWidget(self.betaCalib_label, 1, 1, 1, 1)

        self.t0Calib_label = QLabel(self.groupBox)
        self.t0Calib_label.setObjectName(u"t0Calib_label")

        self.gridLayout.addWidget(self.t0Calib_label, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_radioButton = QRadioButton(self.groupBox)
        self.time_radioButton.setObjectName(u"time_radioButton")

        self.horizontalLayout.addWidget(self.time_radioButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.energy_radioButton = QRadioButton(self.groupBox)
        self.energy_radioButton.setObjectName(u"energy_radioButton")
        self.energy_radioButton.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.energy_radioButton)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.energyMin_lineEdit = QLineEdit(self.groupBox)
        self.energyMin_lineEdit.setObjectName(u"energyMin_lineEdit")
        self.energyMin_lineEdit.setEnabled(False)

        self.verticalLayout_2.addWidget(self.energyMin_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.energyMax_lineEdit = QLineEdit(self.groupBox)
        self.energyMax_lineEdit.setObjectName(u"energyMax_lineEdit")
        self.energyMax_lineEdit.setEnabled(False)

        self.verticalLayout_3.addWidget(self.energyMax_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.energySteps_lineEdit = QLineEdit(self.groupBox)
        self.energySteps_lineEdit.setObjectName(u"energySteps_lineEdit")
        self.energySteps_lineEdit.setEnabled(False)

        self.verticalLayout_4.addWidget(self.energySteps_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.energyStepsNumber_lineEdit = QLineEdit(self.groupBox)
        self.energyStepsNumber_lineEdit.setObjectName(u"energyStepsNumber_lineEdit")
        self.energyStepsNumber_lineEdit.setEnabled(False)

        self.verticalLayout_5.addWidget(self.energyStepsNumber_lineEdit)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.v_optionLayout.addWidget(self.groupBox)

        self.advancedPlot_pushButton = QPushButton(main_panel)
        self.advancedPlot_pushButton.setObjectName(u"advancedPlot_pushButton")

        self.v_optionLayout.addWidget(self.advancedPlot_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.v_optionLayout.addItem(self.verticalSpacer)


        self.h_centralLayout.addLayout(self.v_optionLayout)


        self.horizontalLayout_6.addLayout(self.h_centralLayout)


        self.retranslateUi(main_panel)

        QMetaObject.connectSlotsByName(main_panel)
    # setupUi

    def retranslateUi(self, main_panel):
        main_panel.setWindowTitle(QCoreApplication.translate("main_panel", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_panel", u"Starting folder", None))
#if QT_CONFIG(tooltip)
        self.folderBase_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Use this folder as the base folder when loading data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.forderSelection_toolButton.setText(QCoreApplication.translate("main_panel", u"...", None))
        self.loadSpectrum_pushButton.setText(QCoreApplication.translate("main_panel", u"Load Spectrum", None))
#if QT_CONFIG(tooltip)
        self.fileSelection_listWidget.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>List of selected files:</p><p>- double click on a file to load it</p><p>- right click to remove selected files or clear list</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("main_panel", u"Calibration", None))
#if QT_CONFIG(tooltip)
        self.makeCalibration_pushButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Create a panel to make a calibration from the current signal/FT or from a custom input</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.makeCalibration_pushButton.setText(QCoreApplication.translate("main_panel", u"Make calibration", None))
#if QT_CONFIG(tooltip)
        self.loadCalibration_pushButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Load custom calibration, see examples in Calibration folder if you want to make your own</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.loadCalibration_pushButton.setText(QCoreApplication.translate("main_panel", u"Load calibration", None))
        self.label_5.setText(QCoreApplication.translate("main_panel", u"A", None))
        self.label_6.setText(QCoreApplication.translate("main_panel", u"B", None))
        self.label_7.setText(QCoreApplication.translate("main_panel", u"t0", None))
#if QT_CONFIG(tooltip)
        self.alphaCalib_label.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Coefficient for calibration:</p><p>E = A/(t-t0)^2 + B</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alphaCalib_label.setText("")
#if QT_CONFIG(tooltip)
        self.betaCalib_label.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Coefficient for calibration:</p><p>E = A/(t-t0)^2 + B</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.betaCalib_label.setText("")
#if QT_CONFIG(tooltip)
        self.t0Calib_label.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Coefficient for calibration:</p><p>E = A/(t-t0)^2 + B</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.t0Calib_label.setText("")
#if QT_CONFIG(tooltip)
        self.time_radioButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Time representation</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.time_radioButton.setText(QCoreApplication.translate("main_panel", u"Time", None))
#if QT_CONFIG(tooltip)
        self.energy_radioButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Energy representation</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.energy_radioButton.setText(QCoreApplication.translate("main_panel", u"Energy", None))
        self.label_2.setText(QCoreApplication.translate("main_panel", u"Emin", None))
#if QT_CONFIG(tooltip)
        self.energyMin_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("main_panel", u"Emax", None))
#if QT_CONFIG(tooltip)
        self.energyMax_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("main_panel", u"dE", None))
#if QT_CONFIG(tooltip)
        self.energySteps_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("main_panel", u"nSteps", None))
#if QT_CONFIG(tooltip)
        self.energyStepsNumber_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.advancedPlot_pushButton.setText(QCoreApplication.translate("main_panel", u"Advanced plot", None))
    # retranslateUi

