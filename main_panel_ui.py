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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QToolBox, QToolButton, QVBoxLayout, QWidget)

class Ui_main_panel(object):
    def setupUi(self, main_panel):
        if not main_panel.objectName():
            main_panel.setObjectName(u"main_panel")
        main_panel.resize(602, 767)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_panel.sizePolicy().hasHeightForWidth())
        main_panel.setSizePolicy(sizePolicy)
        self.main_layout = QHBoxLayout(main_panel)
        self.main_layout.setObjectName(u"main_layout")
        self.v_optionLayout = QVBoxLayout()
        self.v_optionLayout.setObjectName(u"v_optionLayout")
        self.toolBox = QToolBox(main_panel)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 582, 320))
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.page_5)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.folderBase_lineEdit = QLineEdit(self.page_5)
        self.folderBase_lineEdit.setObjectName(u"folderBase_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.folderBase_lineEdit.sizePolicy().hasHeightForWidth())
        self.folderBase_lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.folderBase_lineEdit)

        self.forderSelection_toolButton = QToolButton(self.page_5)
        self.forderSelection_toolButton.setObjectName(u"forderSelection_toolButton")

        self.horizontalLayout_3.addWidget(self.forderSelection_toolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.fileSelection_listWidget = QListWidget(self.page_5)
        self.fileSelection_listWidget.setObjectName(u"fileSelection_listWidget")
        sizePolicy.setHeightForWidth(self.fileSelection_listWidget.sizePolicy().hasHeightForWidth())
        self.fileSelection_listWidget.setSizePolicy(sizePolicy)
        self.fileSelection_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.fileSelection_listWidget)

        self.loadSpectrum_pushButton = QPushButton(self.page_5)
        self.loadSpectrum_pushButton.setObjectName(u"loadSpectrum_pushButton")

        self.verticalLayout_2.addWidget(self.loadSpectrum_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_5, u"File selection")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 582, 278))
        self.verticalLayout = QVBoxLayout(self.page_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.makeCalibration_pushButton = QPushButton(self.page_6)
        self.makeCalibration_pushButton.setObjectName(u"makeCalibration_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.makeCalibration_pushButton.sizePolicy().hasHeightForWidth())
        self.makeCalibration_pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.makeCalibration_pushButton)

        self.loadCalibration_pushButton = QPushButton(self.page_6)
        self.loadCalibration_pushButton.setObjectName(u"loadCalibration_pushButton")
        sizePolicy2.setHeightForWidth(self.loadCalibration_pushButton.sizePolicy().hasHeightForWidth())
        self.loadCalibration_pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.loadCalibration_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.t0Calib_label = QLabel(self.page_6)
        self.t0Calib_label.setObjectName(u"t0Calib_label")
        sizePolicy.setHeightForWidth(self.t0Calib_label.sizePolicy().hasHeightForWidth())
        self.t0Calib_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.t0Calib_label, 1, 2, 1, 1)

        self.label_7 = QLabel(self.page_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.alphaCalib_label = QLabel(self.page_6)
        self.alphaCalib_label.setObjectName(u"alphaCalib_label")
        sizePolicy.setHeightForWidth(self.alphaCalib_label.sizePolicy().hasHeightForWidth())
        self.alphaCalib_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.alphaCalib_label, 1, 0, 1, 1)

        self.betaCalib_label = QLabel(self.page_6)
        self.betaCalib_label.setObjectName(u"betaCalib_label")
        sizePolicy.setHeightForWidth(self.betaCalib_label.sizePolicy().hasHeightForWidth())
        self.betaCalib_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.betaCalib_label, 1, 1, 1, 1)

        self.label_5 = QLabel(self.page_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_radioButton = QRadioButton(self.page_6)
        self.time_radioButton.setObjectName(u"time_radioButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.time_radioButton.sizePolicy().hasHeightForWidth())
        self.time_radioButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.time_radioButton)

        self.energy_radioButton = QRadioButton(self.page_6)
        self.energy_radioButton.setObjectName(u"energy_radioButton")
        self.energy_radioButton.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.energy_radioButton.sizePolicy().hasHeightForWidth())
        self.energy_radioButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.energy_radioButton)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.energyMax_lineEdit = QLineEdit(self.page_6)
        self.energyMax_lineEdit.setObjectName(u"energyMax_lineEdit")
        self.energyMax_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.energyMax_lineEdit.sizePolicy().hasHeightForWidth())
        self.energyMax_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.energyMax_lineEdit, 2, 3, 1, 1)

        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.page_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_3, 0, 3, 1, 1)

        self.energyStepsNumber_lineEdit = QLineEdit(self.page_6)
        self.energyStepsNumber_lineEdit.setObjectName(u"energyStepsNumber_lineEdit")
        self.energyStepsNumber_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.energyStepsNumber_lineEdit.sizePolicy().hasHeightForWidth())
        self.energyStepsNumber_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.energyStepsNumber_lineEdit, 2, 5, 1, 1)

        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_8, 0, 5, 1, 1)

        self.energySteps_lineEdit = QLineEdit(self.page_6)
        self.energySteps_lineEdit.setObjectName(u"energySteps_lineEdit")
        self.energySteps_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.energySteps_lineEdit.sizePolicy().hasHeightForWidth())
        self.energySteps_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.energySteps_lineEdit, 2, 4, 1, 1)

        self.energyMin_lineEdit = QLineEdit(self.page_6)
        self.energyMin_lineEdit.setObjectName(u"energyMin_lineEdit")
        self.energyMin_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.energyMin_lineEdit.sizePolicy().hasHeightForWidth())
        self.energyMin_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.energyMin_lineEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.page_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_4, 0, 4, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_6, u"Calibration")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 582, 278))
        sizePolicy.setHeightForWidth(self.page_7.sizePolicy().hasHeightForWidth())
        self.page_7.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.page_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.advancedPlot_pushButton = QPushButton(self.page_7)
        self.advancedPlot_pushButton.setObjectName(u"advancedPlot_pushButton")
        sizePolicy2.setHeightForWidth(self.advancedPlot_pushButton.sizePolicy().hasHeightForWidth())
        self.advancedPlot_pushButton.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.advancedPlot_pushButton)

        self.verticalSpacer_4 = QSpacerItem(20, 226, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.page_7, u"ROI")

        self.v_optionLayout.addWidget(self.toolBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.v_optionLayout.addItem(self.verticalSpacer)


        self.main_layout.addLayout(self.v_optionLayout)

        QWidget.setTabOrder(self.folderBase_lineEdit, self.forderSelection_toolButton)
        QWidget.setTabOrder(self.forderSelection_toolButton, self.fileSelection_listWidget)
        QWidget.setTabOrder(self.fileSelection_listWidget, self.loadSpectrum_pushButton)
        QWidget.setTabOrder(self.loadSpectrum_pushButton, self.makeCalibration_pushButton)
        QWidget.setTabOrder(self.makeCalibration_pushButton, self.loadCalibration_pushButton)
        QWidget.setTabOrder(self.loadCalibration_pushButton, self.time_radioButton)
        QWidget.setTabOrder(self.time_radioButton, self.energy_radioButton)
        QWidget.setTabOrder(self.energy_radioButton, self.energyMin_lineEdit)
        QWidget.setTabOrder(self.energyMin_lineEdit, self.energyMax_lineEdit)
        QWidget.setTabOrder(self.energyMax_lineEdit, self.energySteps_lineEdit)
        QWidget.setTabOrder(self.energySteps_lineEdit, self.energyStepsNumber_lineEdit)

        self.retranslateUi(main_panel)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_panel)
    # setupUi

    def retranslateUi(self, main_panel):
        main_panel.setWindowTitle(QCoreApplication.translate("main_panel", u"Form", None))
        self.label.setText(QCoreApplication.translate("main_panel", u"Starting folder", None))
#if QT_CONFIG(tooltip)
        self.folderBase_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Use this folder as the base folder when loading data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.forderSelection_toolButton.setText(QCoreApplication.translate("main_panel", u"...", None))
#if QT_CONFIG(tooltip)
        self.fileSelection_listWidget.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>List of selected files:</p><p>- double click on a file to load it</p><p>- right click to remove selected files or clear list</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.loadSpectrum_pushButton.setText(QCoreApplication.translate("main_panel", u"Load Spectrum", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("main_panel", u"File selection", None))
#if QT_CONFIG(tooltip)
        self.makeCalibration_pushButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Create a panel to make a calibration from the current signal/FT or from a custom input</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.makeCalibration_pushButton.setText(QCoreApplication.translate("main_panel", u"Make calibration", None))
#if QT_CONFIG(tooltip)
        self.loadCalibration_pushButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Load custom calibration, see examples in Calibration folder if you want to make your own</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.loadCalibration_pushButton.setText(QCoreApplication.translate("main_panel", u"Load calibration", None))
#if QT_CONFIG(tooltip)
        self.t0Calib_label.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Coefficient for calibration:</p><p>E = A/(t-t0)^2 + B</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.t0Calib_label.setText("")
        self.label_7.setText(QCoreApplication.translate("main_panel", u"t0", None))
        self.label_6.setText(QCoreApplication.translate("main_panel", u"B", None))
#if QT_CONFIG(tooltip)
        self.alphaCalib_label.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Coefficient for calibration:</p><p>E = A/(t-t0)^2 + B</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alphaCalib_label.setText("")
#if QT_CONFIG(tooltip)
        self.betaCalib_label.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Coefficient for calibration:</p><p>E = A/(t-t0)^2 + B</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.betaCalib_label.setText("")
        self.label_5.setText(QCoreApplication.translate("main_panel", u"A", None))
#if QT_CONFIG(tooltip)
        self.time_radioButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Time representation</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.time_radioButton.setText(QCoreApplication.translate("main_panel", u"Time", None))
#if QT_CONFIG(tooltip)
        self.energy_radioButton.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Energy representation</p><p>You first need to load a calibration and to define the linear axis that you are looking for to toggle it</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.energy_radioButton.setText(QCoreApplication.translate("main_panel", u"Energy", None))
#if QT_CONFIG(tooltip)
        self.energyMax_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("main_panel", u"Emin", None))
        self.label_3.setText(QCoreApplication.translate("main_panel", u"Emax", None))
#if QT_CONFIG(tooltip)
        self.energyStepsNumber_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("main_panel", u"nSteps", None))
#if QT_CONFIG(tooltip)
        self.energySteps_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.energyMin_lineEdit.setToolTip(QCoreApplication.translate("main_panel", u"<html><head/><body><p>Maximum energy to be plotted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("main_panel", u"dE", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("main_panel", u"Calibration", None))
        self.advancedPlot_pushButton.setText(QCoreApplication.translate("main_panel", u"Advanced plot", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("main_panel", u"ROI", None))
    # retranslateUi

