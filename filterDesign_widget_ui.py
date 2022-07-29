# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filterDesign_widget.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FilterWidget(object):
    def setupUi(self, FilterWidget):
        if not FilterWidget.objectName():
            FilterWidget.setObjectName(u"FilterWidget")
        FilterWidget.resize(385, 356)
        FilterWidget.setLocale(QLocale(QLocale.C, QLocale.AnyTerritory))
        self.verticalLayout_3 = QVBoxLayout(FilterWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lowerPassBand_label = QLabel(FilterWidget)
        self.lowerPassBand_label.setObjectName(u"lowerPassBand_label")
        self.lowerPassBand_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lowerPassBand_label, 5, 0, 1, 2)

        self.lowerStopBand_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.lowerStopBand_doubleSpinBox.setObjectName(u"lowerStopBand_doubleSpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerStopBand_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.lowerStopBand_doubleSpinBox.setSizePolicy(sizePolicy)
        self.lowerStopBand_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lowerStopBand_doubleSpinBox.setKeyboardTracking(False)
        self.lowerStopBand_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.lowerStopBand_doubleSpinBox.setMaximum(10000000.000000000000000)
        self.lowerStopBand_doubleSpinBox.setValue(0.300000000000000)

        self.gridLayout.addWidget(self.lowerStopBand_doubleSpinBox, 5, 4, 1, 1)

        self.filterRole_comboBox = QComboBox(FilterWidget)
        self.filterRole_comboBox.addItem("")
        self.filterRole_comboBox.addItem("")
        self.filterRole_comboBox.addItem("")
        self.filterRole_comboBox.addItem("")
        self.filterRole_comboBox.setObjectName(u"filterRole_comboBox")

        self.gridLayout.addWidget(self.filterRole_comboBox, 2, 3, 1, 2)

        self.label_2 = QLabel(FilterWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)

        self.label_7 = QLabel(FilterWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 2)

        self.minLossStopBand_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.minLossStopBand_doubleSpinBox.setObjectName(u"minLossStopBand_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.minLossStopBand_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.minLossStopBand_doubleSpinBox.setSizePolicy(sizePolicy)
        self.minLossStopBand_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.minLossStopBand_doubleSpinBox.setKeyboardTracking(False)
        self.minLossStopBand_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.minLossStopBand_doubleSpinBox.setMaximum(10000000.000000000000000)
        self.minLossStopBand_doubleSpinBox.setValue(40.000000000000000)

        self.gridLayout.addWidget(self.minLossStopBand_doubleSpinBox, 7, 4, 1, 1)

        self.label_4 = QLabel(FilterWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 2)

        self.lowerPassBand_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.lowerPassBand_doubleSpinBox.setObjectName(u"lowerPassBand_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.lowerPassBand_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.lowerPassBand_doubleSpinBox.setSizePolicy(sizePolicy)
        self.lowerPassBand_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.lowerPassBand_doubleSpinBox.setKeyboardTracking(False)
        self.lowerPassBand_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.lowerPassBand_doubleSpinBox.setMaximum(10000000.000000000000000)
        self.lowerPassBand_doubleSpinBox.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.lowerPassBand_doubleSpinBox, 5, 2, 1, 1)

        self.upperStopBand_label = QLabel(FilterWidget)
        self.upperStopBand_label.setObjectName(u"upperStopBand_label")
        self.upperStopBand_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.upperStopBand_label, 6, 3, 1, 1)

        self.upperPassBand_label = QLabel(FilterWidget)
        self.upperPassBand_label.setObjectName(u"upperPassBand_label")
        self.upperPassBand_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.upperPassBand_label, 6, 0, 1, 2)

        self.label_5 = QLabel(FilterWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 2)

        self.upperPassBand_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.upperPassBand_doubleSpinBox.setObjectName(u"upperPassBand_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.upperPassBand_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.upperPassBand_doubleSpinBox.setSizePolicy(sizePolicy)
        self.upperPassBand_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.upperPassBand_doubleSpinBox.setKeyboardTracking(False)
        self.upperPassBand_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.upperPassBand_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.upperPassBand_doubleSpinBox, 6, 2, 1, 1)

        self.filterType_comboBox = QComboBox(FilterWidget)
        self.filterType_comboBox.addItem("")
        self.filterType_comboBox.addItem("")
        self.filterType_comboBox.addItem("")
        self.filterType_comboBox.addItem("")
        self.filterType_comboBox.addItem("")
        self.filterType_comboBox.setObjectName(u"filterType_comboBox")

        self.gridLayout.addWidget(self.filterType_comboBox, 2, 0, 1, 3)

        self.lowerStopBand_label = QLabel(FilterWidget)
        self.lowerStopBand_label.setObjectName(u"lowerStopBand_label")
        self.lowerStopBand_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lowerStopBand_label, 5, 3, 1, 1)

        self.upperStopBand_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.upperStopBand_doubleSpinBox.setObjectName(u"upperStopBand_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.upperStopBand_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.upperStopBand_doubleSpinBox.setSizePolicy(sizePolicy)
        self.upperStopBand_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.upperStopBand_doubleSpinBox.setKeyboardTracking(False)
        self.upperStopBand_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.upperStopBand_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.upperStopBand_doubleSpinBox, 6, 4, 1, 1)

        self.label_6 = QLabel(FilterWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 3)

        self.label_3 = QLabel(FilterWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 7, 3, 1, 1)

        self.maxLossPassBand_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.maxLossPassBand_doubleSpinBox.setObjectName(u"maxLossPassBand_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.maxLossPassBand_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.maxLossPassBand_doubleSpinBox.setSizePolicy(sizePolicy)
        self.maxLossPassBand_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.maxLossPassBand_doubleSpinBox.setKeyboardTracking(False)
        self.maxLossPassBand_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.maxLossPassBand_doubleSpinBox.setMaximum(10000000.000000000000000)
        self.maxLossPassBand_doubleSpinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.maxLossPassBand_doubleSpinBox.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.maxLossPassBand_doubleSpinBox, 7, 2, 1, 1)

        self.samplingFrequency_doubleSpinBox = QDoubleSpinBox(FilterWidget)
        self.samplingFrequency_doubleSpinBox.setObjectName(u"samplingFrequency_doubleSpinBox")
        sizePolicy.setHeightForWidth(self.samplingFrequency_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.samplingFrequency_doubleSpinBox.setSizePolicy(sizePolicy)
        self.samplingFrequency_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.samplingFrequency_doubleSpinBox.setKeyboardTracking(False)
        self.samplingFrequency_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.samplingFrequency_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.samplingFrequency_doubleSpinBox, 8, 3, 1, 2)

        self.label_12 = QLabel(FilterWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 3)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.groupBox = QGroupBox(FilterWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.digital_radioButton = QRadioButton(self.groupBox)
        self.digital_radioButton.setObjectName(u"digital_radioButton")
        self.digital_radioButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.digital_radioButton)

        self.analog_radioButton = QRadioButton(self.groupBox)
        self.analog_radioButton.setObjectName(u"analog_radioButton")

        self.verticalLayout_2.addWidget(self.analog_radioButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.outputFilter_comboBox = QComboBox(self.groupBox)
        self.outputFilter_comboBox.addItem("")
        self.outputFilter_comboBox.addItem("")
        self.outputFilter_comboBox.addItem("")
        self.outputFilter_comboBox.setObjectName(u"outputFilter_comboBox")

        self.verticalLayout.addWidget(self.outputFilter_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.doPlot_pushButton = QPushButton(FilterWidget)
        self.doPlot_pushButton.setObjectName(u"doPlot_pushButton")

        self.verticalLayout_3.addWidget(self.doPlot_pushButton)

        QWidget.setTabOrder(self.filterType_comboBox, self.filterRole_comboBox)
        QWidget.setTabOrder(self.filterRole_comboBox, self.lowerPassBand_doubleSpinBox)
        QWidget.setTabOrder(self.lowerPassBand_doubleSpinBox, self.lowerStopBand_doubleSpinBox)
        QWidget.setTabOrder(self.lowerStopBand_doubleSpinBox, self.upperPassBand_doubleSpinBox)
        QWidget.setTabOrder(self.upperPassBand_doubleSpinBox, self.upperStopBand_doubleSpinBox)
        QWidget.setTabOrder(self.upperStopBand_doubleSpinBox, self.maxLossPassBand_doubleSpinBox)
        QWidget.setTabOrder(self.maxLossPassBand_doubleSpinBox, self.minLossStopBand_doubleSpinBox)
        QWidget.setTabOrder(self.minLossStopBand_doubleSpinBox, self.samplingFrequency_doubleSpinBox)
        QWidget.setTabOrder(self.samplingFrequency_doubleSpinBox, self.digital_radioButton)
        QWidget.setTabOrder(self.digital_radioButton, self.analog_radioButton)
        QWidget.setTabOrder(self.analog_radioButton, self.outputFilter_comboBox)
        QWidget.setTabOrder(self.outputFilter_comboBox, self.doPlot_pushButton)

        self.retranslateUi(FilterWidget)

        QMetaObject.connectSlotsByName(FilterWidget)
    # setupUi

    def retranslateUi(self, FilterWidget):
        FilterWidget.setWindowTitle(QCoreApplication.translate("FilterWidget", u"Form", None))
        self.lowerPassBand_label.setText(QCoreApplication.translate("FilterWidget", u"Lower", None))
        self.lowerStopBand_doubleSpinBox.setSuffix("")
        self.filterRole_comboBox.setItemText(0, QCoreApplication.translate("FilterWidget", u"Low Pass", None))
        self.filterRole_comboBox.setItemText(1, QCoreApplication.translate("FilterWidget", u"High Pass", None))
        self.filterRole_comboBox.setItemText(2, QCoreApplication.translate("FilterWidget", u"Band Pass", None))
        self.filterRole_comboBox.setItemText(3, QCoreApplication.translate("FilterWidget", u"Band Stop", None))

#if QT_CONFIG(tooltip)
        self.filterRole_comboBox.setToolTip(QCoreApplication.translate("FilterWidget", u"<html><head/><body><p>Filter role:</p><p>- LowPass: lower pass band &lt; lower stop band</p><p>- HighPass: upper pass band &gt; upper stop band</p><p>- BandPass: lower pass band &gt; lower stop band &amp; upper pass band &lt; upper stop band</p><p>- BandStop: lower pass band &lt; lower stop band &amp; upper pass band &gt; upper stop band</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("FilterWidget", u"Pass band", None))
        self.label_7.setText(QCoreApplication.translate("FilterWidget", u"Role", None))
        self.minLossStopBand_doubleSpinBox.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("FilterWidget", u"gpass", None))
        self.lowerPassBand_doubleSpinBox.setSuffix("")
        self.upperStopBand_label.setText(QCoreApplication.translate("FilterWidget", u"Upper", None))
        self.upperPassBand_label.setText(QCoreApplication.translate("FilterWidget", u"Upper", None))
        self.label_5.setText(QCoreApplication.translate("FilterWidget", u"Stop band", None))
        self.upperPassBand_doubleSpinBox.setSuffix("")
        self.filterType_comboBox.setItemText(0, QCoreApplication.translate("FilterWidget", u"Butterworth", None))
        self.filterType_comboBox.setItemText(1, QCoreApplication.translate("FilterWidget", u"Chebyshev I", None))
        self.filterType_comboBox.setItemText(2, QCoreApplication.translate("FilterWidget", u"Chebyshev II", None))
        self.filterType_comboBox.setItemText(3, QCoreApplication.translate("FilterWidget", u"Cauer/elliptic", None))
        self.filterType_comboBox.setItemText(4, QCoreApplication.translate("FilterWidget", u"Bessel/Thomson", None))

        self.lowerStopBand_label.setText(QCoreApplication.translate("FilterWidget", u"Lower", None))
        self.upperStopBand_doubleSpinBox.setSuffix("")
        self.label_6.setText(QCoreApplication.translate("FilterWidget", u"Type", None))
        self.label_3.setText(QCoreApplication.translate("FilterWidget", u"gstop", None))
        self.maxLossPassBand_doubleSpinBox.setSuffix("")
        self.samplingFrequency_doubleSpinBox.setSuffix("")
        self.label_12.setText(QCoreApplication.translate("FilterWidget", u"Sampling frequency", None))
        self.groupBox.setTitle(QCoreApplication.translate("FilterWidget", u"Output filter", None))
        self.digital_radioButton.setText(QCoreApplication.translate("FilterWidget", u"Digital", None))
        self.analog_radioButton.setText(QCoreApplication.translate("FilterWidget", u"Analog", None))
        self.label_13.setText(QCoreApplication.translate("FilterWidget", u"Filter form", None))
        self.outputFilter_comboBox.setItemText(0, QCoreApplication.translate("FilterWidget", u"numerator/denominator (b,a)", None))
        self.outputFilter_comboBox.setItemText(1, QCoreApplication.translate("FilterWidget", u"second-order sections (sos)", None))
        self.outputFilter_comboBox.setItemText(2, QCoreApplication.translate("FilterWidget", u"pole-zero (z,p,k)", None))

        self.doPlot_pushButton.setText(QCoreApplication.translate("FilterWidget", u"PushButton", None))
    # retranslateUi

