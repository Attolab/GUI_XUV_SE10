# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signal_processing_toolbox.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_SignalProcessingToolbox(object):
    def setupUi(self, SignalProcessingToolbox):
        if not SignalProcessingToolbox.objectName():
            SignalProcessingToolbox.setObjectName(u"SignalProcessingToolbox")
        SignalProcessingToolbox.resize(840, 513)
        self.verticalLayout_3 = QVBoxLayout(SignalProcessingToolbox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_7 = QGroupBox(SignalProcessingToolbox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.groupBox_7)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.inputAxis0Start_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.inputAxis0Start_doubleSpinBox.setObjectName(u"inputAxis0Start_doubleSpinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputAxis0Start_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.inputAxis0Start_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.inputAxis0Start_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.inputAxis0Start_doubleSpinBox.setKeyboardTracking(False)
        self.inputAxis0Start_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.inputAxis0Start_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.inputAxis0Start_doubleSpinBox)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.inputAxis0End_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.inputAxis0End_doubleSpinBox.setObjectName(u"inputAxis0End_doubleSpinBox")
        sizePolicy1.setHeightForWidth(self.inputAxis0End_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.inputAxis0End_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.inputAxis0End_doubleSpinBox.setKeyboardTracking(False)
        self.inputAxis0End_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.inputAxis0End_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.inputAxis0End_doubleSpinBox)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.inputAxis0Mult_lineEdit = QLineEdit(self.groupBox)
        self.inputAxis0Mult_lineEdit.setObjectName(u"inputAxis0Mult_lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.inputAxis0Mult_lineEdit.sizePolicy().hasHeightForWidth())
        self.inputAxis0Mult_lineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.inputAxis0Mult_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.inputAxis0Add_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.inputAxis0Add_doubleSpinBox.setObjectName(u"inputAxis0Add_doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.inputAxis0Add_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.inputAxis0Add_doubleSpinBox.setSizePolicy(sizePolicy2)
        self.inputAxis0Add_doubleSpinBox.setKeyboardTracking(False)
        self.inputAxis0Add_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.inputAxis0Add_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_7.addWidget(self.inputAxis0Add_doubleSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.inputAxis1Start_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.inputAxis1Start_doubleSpinBox.setObjectName(u"inputAxis1Start_doubleSpinBox")
        sizePolicy1.setHeightForWidth(self.inputAxis1Start_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.inputAxis1Start_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.inputAxis1Start_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.inputAxis1Start_doubleSpinBox.setKeyboardTracking(False)
        self.inputAxis1Start_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.inputAxis1Start_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_5.addWidget(self.inputAxis1Start_doubleSpinBox)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.inputAxis1End_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.inputAxis1End_doubleSpinBox.setObjectName(u"inputAxis1End_doubleSpinBox")
        sizePolicy1.setHeightForWidth(self.inputAxis1End_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.inputAxis1End_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.inputAxis1End_doubleSpinBox.setKeyboardTracking(False)
        self.inputAxis1End_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.inputAxis1End_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_5.addWidget(self.inputAxis1End_doubleSpinBox)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.inputAxis1Mult_lineEdit = QLineEdit(self.groupBox)
        self.inputAxis1Mult_lineEdit.setObjectName(u"inputAxis1Mult_lineEdit")
        sizePolicy2.setHeightForWidth(self.inputAxis1Mult_lineEdit.sizePolicy().hasHeightForWidth())
        self.inputAxis1Mult_lineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.inputAxis1Mult_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_8.addWidget(self.label_17)

        self.inputAxis1Add_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.inputAxis1Add_doubleSpinBox.setObjectName(u"inputAxis1Add_doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.inputAxis1Add_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.inputAxis1Add_doubleSpinBox.setSizePolicy(sizePolicy2)
        self.inputAxis1Add_doubleSpinBox.setKeyboardTracking(False)
        self.inputAxis1Add_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.inputAxis1Add_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_8.addWidget(self.inputAxis1Add_doubleSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.groupBox_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.interpolation_comboBox = QComboBox(self.groupBox_2)
        self.interpolation_comboBox.addItem("")
        self.interpolation_comboBox.addItem("")
        self.interpolation_comboBox.addItem("")
        self.interpolation_comboBox.setObjectName(u"interpolation_comboBox")
        sizePolicy1.setHeightForWidth(self.interpolation_comboBox.sizePolicy().hasHeightForWidth())
        self.interpolation_comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.interpolation_comboBox)

        self.interpolation_spinBox = QSpinBox(self.groupBox_2)
        self.interpolation_spinBox.setObjectName(u"interpolation_spinBox")
        sizePolicy1.setHeightForWidth(self.interpolation_spinBox.sizePolicy().hasHeightForWidth())
        self.interpolation_spinBox.setSizePolicy(sizePolicy1)
        self.interpolation_spinBox.setKeyboardTracking(False)
        self.interpolation_spinBox.setMaximum(10000000)

        self.horizontalLayout_4.addWidget(self.interpolation_spinBox)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.removeBackground_comboBox = QComboBox(self.groupBox_2)
        self.removeBackground_comboBox.addItem("")
        self.removeBackground_comboBox.addItem("")
        self.removeBackground_comboBox.addItem("")
        self.removeBackground_comboBox.addItem("")
        self.removeBackground_comboBox.addItem("")
        self.removeBackground_comboBox.setObjectName(u"removeBackground_comboBox")
        sizePolicy1.setHeightForWidth(self.removeBackground_comboBox.sizePolicy().hasHeightForWidth())
        self.removeBackground_comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.removeBackground_comboBox)

        self.removeBackground_doubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.removeBackground_doubleSpinBox.setObjectName(u"removeBackground_doubleSpinBox")
        sizePolicy1.setHeightForWidth(self.removeBackground_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.removeBackground_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.removeBackground_doubleSpinBox.setKeyboardTracking(False)
        self.removeBackground_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.removeBackground_doubleSpinBox.setMaximum(10000000.000000000000000)
        self.removeBackground_doubleSpinBox.setValue(0.000000000000000)

        self.horizontalLayout_6.addWidget(self.removeBackground_doubleSpinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_30)

        self.smooth_comboBox = QComboBox(self.groupBox_2)
        self.smooth_comboBox.addItem("")
        self.smooth_comboBox.setObjectName(u"smooth_comboBox")
        self.smooth_comboBox.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.smooth_comboBox.sizePolicy().hasHeightForWidth())
        self.smooth_comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.smooth_comboBox)

        self.smooth_spinBox = QSpinBox(self.groupBox_2)
        self.smooth_spinBox.setObjectName(u"smooth_spinBox")
        self.smooth_spinBox.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.smooth_spinBox.sizePolicy().hasHeightForWidth())
        self.smooth_spinBox.setSizePolicy(sizePolicy1)
        self.smooth_spinBox.setKeyboardTracking(False)
        self.smooth_spinBox.setMaximum(10000000)

        self.horizontalLayout_17.addWidget(self.smooth_spinBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.FT_zeropaddingpower2_spinBox = QSpinBox(self.groupBox_3)
        self.FT_zeropaddingpower2_spinBox.setObjectName(u"FT_zeropaddingpower2_spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.FT_zeropaddingpower2_spinBox.sizePolicy().hasHeightForWidth())
        self.FT_zeropaddingpower2_spinBox.setSizePolicy(sizePolicy3)
        self.FT_zeropaddingpower2_spinBox.setAutoFillBackground(False)
        self.FT_zeropaddingpower2_spinBox.setKeyboardTracking(False)
        self.FT_zeropaddingpower2_spinBox.setMaximum(10000000)

        self.gridLayout.addWidget(self.FT_zeropaddingpower2_spinBox, 2, 1, 1, 1)

        self.FT_zeropadding_comboBox = QComboBox(self.groupBox_3)
        self.FT_zeropadding_comboBox.addItem("")
        self.FT_zeropadding_comboBox.addItem("")
        self.FT_zeropadding_comboBox.addItem("")
        self.FT_zeropadding_comboBox.addItem("")
        self.FT_zeropadding_comboBox.setObjectName(u"FT_zeropadding_comboBox")
        sizePolicy1.setHeightForWidth(self.FT_zeropadding_comboBox.sizePolicy().hasHeightForWidth())
        self.FT_zeropadding_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.FT_zeropadding_comboBox, 1, 1, 1, 1)

        self.FT_zeropadding_spinBox = QSpinBox(self.groupBox_3)
        self.FT_zeropadding_spinBox.setObjectName(u"FT_zeropadding_spinBox")
        sizePolicy3.setHeightForWidth(self.FT_zeropadding_spinBox.sizePolicy().hasHeightForWidth())
        self.FT_zeropadding_spinBox.setSizePolicy(sizePolicy3)
        self.FT_zeropadding_spinBox.setKeyboardTracking(False)
        self.FT_zeropadding_spinBox.setMaximum(10000000)

        self.gridLayout.addWidget(self.FT_zeropadding_spinBox, 1, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.FT_window_comboBox = QComboBox(self.groupBox_3)
        self.FT_window_comboBox.addItem("")
        self.FT_window_comboBox.addItem("")
        self.FT_window_comboBox.addItem("")
        self.FT_window_comboBox.addItem("")
        self.FT_window_comboBox.addItem("")
        self.FT_window_comboBox.setObjectName(u"FT_window_comboBox")
        sizePolicy2.setHeightForWidth(self.FT_window_comboBox.sizePolicy().hasHeightForWidth())
        self.FT_window_comboBox.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.FT_window_comboBox, 0, 1, 1, 2)


        self.horizontalLayout_16.addLayout(self.gridLayout)

        self.line_4 = QFrame(self.groupBox_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_24)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.outputAxisStart_doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.outputAxisStart_doubleSpinBox.setObjectName(u"outputAxisStart_doubleSpinBox")
        sizePolicy1.setHeightForWidth(self.outputAxisStart_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.outputAxisStart_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.outputAxisStart_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.outputAxisStart_doubleSpinBox.setKeyboardTracking(False)
        self.outputAxisStart_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.outputAxisStart_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_13.addWidget(self.outputAxisStart_doubleSpinBox)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.label_26)

        self.outputAxisEnd_doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.outputAxisEnd_doubleSpinBox.setObjectName(u"outputAxisEnd_doubleSpinBox")
        sizePolicy1.setHeightForWidth(self.outputAxisEnd_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.outputAxisEnd_doubleSpinBox.setSizePolicy(sizePolicy1)
        self.outputAxisEnd_doubleSpinBox.setKeyboardTracking(False)
        self.outputAxisEnd_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.outputAxisEnd_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.horizontalLayout_13.addWidget(self.outputAxisEnd_doubleSpinBox)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.label_27)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_14.addWidget(self.label_28)

        self.outputAxisMult_lineEdit = QLineEdit(self.groupBox_3)
        self.outputAxisMult_lineEdit.setObjectName(u"outputAxisMult_lineEdit")

        self.horizontalLayout_14.addWidget(self.outputAxisMult_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_16.addLayout(self.verticalLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.verticalLayout_3.addWidget(self.groupBox_7)

        QWidget.setTabOrder(self.inputAxis0Start_doubleSpinBox, self.inputAxis0End_doubleSpinBox)
        QWidget.setTabOrder(self.inputAxis0End_doubleSpinBox, self.interpolation_comboBox)
        QWidget.setTabOrder(self.interpolation_comboBox, self.interpolation_spinBox)
        QWidget.setTabOrder(self.interpolation_spinBox, self.removeBackground_comboBox)
        QWidget.setTabOrder(self.removeBackground_comboBox, self.removeBackground_doubleSpinBox)
        QWidget.setTabOrder(self.removeBackground_doubleSpinBox, self.FT_window_comboBox)
        QWidget.setTabOrder(self.FT_window_comboBox, self.FT_zeropadding_comboBox)
        QWidget.setTabOrder(self.FT_zeropadding_comboBox, self.FT_zeropadding_spinBox)
        QWidget.setTabOrder(self.FT_zeropadding_spinBox, self.FT_zeropaddingpower2_spinBox)

        self.retranslateUi(SignalProcessingToolbox)

        self.FT_window_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SignalProcessingToolbox)
    # setupUi

    def retranslateUi(self, SignalProcessingToolbox):
        SignalProcessingToolbox.setWindowTitle(QCoreApplication.translate("SignalProcessingToolbox", u"Form", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("SignalProcessingToolbox", u"Configuration", None))
        self.groupBox.setTitle(QCoreApplication.translate("SignalProcessingToolbox", u"Axis Manipulation", None))
        self.label_13.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Periodic Axis (XAxis)", None))
        self.label.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Filter", None))
        self.inputAxis0Start_doubleSpinBox.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("SignalProcessingToolbox", u"-", None))
        self.label_4.setText(QCoreApplication.translate("SignalProcessingToolbox", u"units", None))
        self.label_10.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Multiplicative factor", None))
        self.inputAxis0Mult_lineEdit.setText(QCoreApplication.translate("SignalProcessingToolbox", u"1.0", None))
        self.label_14.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Offset", None))
        self.label_12.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Parameter Axis (YAxis)", None))
        self.label_7.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Filter", None))
        self.inputAxis1Start_doubleSpinBox.setSuffix("")
        self.label_8.setText(QCoreApplication.translate("SignalProcessingToolbox", u"-", None))
        self.label_9.setText(QCoreApplication.translate("SignalProcessingToolbox", u"units", None))
        self.label_11.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Multiplicative factor", None))
        self.inputAxis1Mult_lineEdit.setText(QCoreApplication.translate("SignalProcessingToolbox", u"1.0", None))
        self.label_17.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Offset", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SignalProcessingToolbox", u"Signal manipulation", None))
        self.label_3.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Interpolation", None))
        self.interpolation_comboBox.setItemText(0, QCoreApplication.translate("SignalProcessingToolbox", u"No Interpolation", None))
        self.interpolation_comboBox.setItemText(1, QCoreApplication.translate("SignalProcessingToolbox", u"Linear", None))
        self.interpolation_comboBox.setItemText(2, QCoreApplication.translate("SignalProcessingToolbox", u"Cubic", None))

        self.label_6.setText(QCoreApplication.translate("SignalProcessingToolbox", u"number of points", None))
        self.label_5.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Remove background", None))
        self.removeBackground_comboBox.setItemText(0, QCoreApplication.translate("SignalProcessingToolbox", u"Mean value", None))
        self.removeBackground_comboBox.setItemText(1, QCoreApplication.translate("SignalProcessingToolbox", u"First value", None))
        self.removeBackground_comboBox.setItemText(2, QCoreApplication.translate("SignalProcessingToolbox", u"End value", None))
        self.removeBackground_comboBox.setItemText(3, QCoreApplication.translate("SignalProcessingToolbox", u"Min value", None))
        self.removeBackground_comboBox.setItemText(4, QCoreApplication.translate("SignalProcessingToolbox", u"Custom value", None))

        self.label_30.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Smooth signal", None))
        self.smooth_comboBox.setItemText(0, QCoreApplication.translate("SignalProcessingToolbox", u"No Smooth", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("SignalProcessingToolbox", u"Fourier Transform", None))
        self.FT_zeropadding_comboBox.setItemText(0, QCoreApplication.translate("SignalProcessingToolbox", u"Next Power of 2 (from input)", None))
        self.FT_zeropadding_comboBox.setItemText(1, QCoreApplication.translate("SignalProcessingToolbox", u"Power of 2", None))
        self.FT_zeropadding_comboBox.setItemText(2, QCoreApplication.translate("SignalProcessingToolbox", u"Identical as input", None))
        self.FT_zeropadding_comboBox.setItemText(3, QCoreApplication.translate("SignalProcessingToolbox", u"Custom", None))

        self.label_16.setText(QCoreApplication.translate("SignalProcessingToolbox", u"0-padding", None))
        self.label_15.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Window", None))
        self.FT_window_comboBox.setItemText(0, QCoreApplication.translate("SignalProcessingToolbox", u"Rectangle", None))
        self.FT_window_comboBox.setItemText(1, QCoreApplication.translate("SignalProcessingToolbox", u"Hann", None))
        self.FT_window_comboBox.setItemText(2, QCoreApplication.translate("SignalProcessingToolbox", u"Hamming", None))
        self.FT_window_comboBox.setItemText(3, QCoreApplication.translate("SignalProcessingToolbox", u"Kaiser", None))
        self.FT_window_comboBox.setItemText(4, QCoreApplication.translate("SignalProcessingToolbox", u"Blackman-Harris", None))

        self.label_24.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Frequency Axis (XAxis)", None))
        self.label_25.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Filter", None))
        self.outputAxisStart_doubleSpinBox.setSuffix("")
        self.label_26.setText(QCoreApplication.translate("SignalProcessingToolbox", u"-", None))
        self.label_27.setText(QCoreApplication.translate("SignalProcessingToolbox", u"units-1", None))
        self.label_28.setText(QCoreApplication.translate("SignalProcessingToolbox", u"Multiplicative factor", None))
        self.outputAxisMult_lineEdit.setText(QCoreApplication.translate("SignalProcessingToolbox", u"1.0", None))
    # retranslateUi

