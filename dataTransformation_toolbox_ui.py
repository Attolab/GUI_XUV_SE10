# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataTransformation_toolbox.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

from pyqtgraph.parametertree import ParameterTree

class Ui_dataTransformationToolbox(object):
    def setupUi(self, dataTransformationToolbox):
        if not dataTransformationToolbox.objectName():
            dataTransformationToolbox.setObjectName(u"dataTransformationToolbox")
        dataTransformationToolbox.resize(673, 286)
        self.horizontalLayout_5 = QHBoxLayout(dataTransformationToolbox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(dataTransformationToolbox)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.basicOperation_tab = QWidget()
        self.basicOperation_tab.setObjectName(u"basicOperation_tab")
        self.verticalLayout_4 = QVBoxLayout(self.basicOperation_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.basicOperationPredef_comboBox = QComboBox(self.basicOperation_tab)
        self.basicOperationPredef_comboBox.addItem("")
        self.basicOperationPredef_comboBox.addItem("")
        self.basicOperationPredef_comboBox.addItem("")
        self.basicOperationPredef_comboBox.addItem("")
        self.basicOperationPredef_comboBox.addItem("")
        self.basicOperationPredef_comboBox.setObjectName(u"basicOperationPredef_comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.basicOperationPredef_comboBox.sizePolicy().hasHeightForWidth())
        self.basicOperationPredef_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.basicOperationPredef_comboBox, 2, 1, 1, 1)

        self.basicOperationChoice_comboBox = QComboBox(self.basicOperation_tab)
        self.basicOperationChoice_comboBox.addItem("")
        self.basicOperationChoice_comboBox.addItem("")
        self.basicOperationChoice_comboBox.addItem("")
        self.basicOperationChoice_comboBox.addItem("")
        self.basicOperationChoice_comboBox.setObjectName(u"basicOperationChoice_comboBox")

        self.gridLayout_3.addWidget(self.basicOperationChoice_comboBox, 2, 0, 1, 1)

        self.basicOperation_doubleSpinBox = QDoubleSpinBox(self.basicOperation_tab)
        self.basicOperation_doubleSpinBox.setObjectName(u"basicOperation_doubleSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.basicOperation_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.basicOperation_doubleSpinBox.setSizePolicy(sizePolicy2)
        self.basicOperation_doubleSpinBox.setKeyboardTracking(False)
        self.basicOperation_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.basicOperation_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout_3.addWidget(self.basicOperation_doubleSpinBox, 2, 2, 1, 1)

        self.label_20 = QLabel(self.basicOperation_tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 4)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.basicOperation_tab, "")
        self.filterOperation_tab = QWidget()
        self.filterOperation_tab.setObjectName(u"filterOperation_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.filterOperation_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.filterOperation_tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 1, 6, 1, 1)

        self.label_4 = QLabel(self.filterOperation_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.filterStartBelongTo_comboBox = QComboBox(self.filterOperation_tab)
        self.filterStartBelongTo_comboBox.addItem("")
        self.filterStartBelongTo_comboBox.addItem("")
        self.filterStartBelongTo_comboBox.setObjectName(u"filterStartBelongTo_comboBox")

        self.gridLayout.addWidget(self.filterStartBelongTo_comboBox, 2, 2, 1, 1)

        self.filterEnd__doubleSpinBox = QDoubleSpinBox(self.filterOperation_tab)
        self.filterEnd__doubleSpinBox.setObjectName(u"filterEnd__doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.filterEnd__doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.filterEnd__doubleSpinBox.setSizePolicy(sizePolicy2)
        self.filterEnd__doubleSpinBox.setKeyboardTracking(False)
        self.filterEnd__doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.filterEnd__doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.filterEnd__doubleSpinBox, 2, 4, 1, 1)

        self.filterFlip_comboBox = QComboBox(self.filterOperation_tab)
        self.filterFlip_comboBox.addItem("")
        self.filterFlip_comboBox.addItem("")
        self.filterFlip_comboBox.setObjectName(u"filterFlip_comboBox")
        sizePolicy1.setHeightForWidth(self.filterFlip_comboBox.sizePolicy().hasHeightForWidth())
        self.filterFlip_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.filterFlip_comboBox, 2, 6, 1, 1)

        self.label_7 = QLabel(self.filterOperation_tab)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)

        self.label_2 = QLabel(self.filterOperation_tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.filterStart_doubleSpinBox = QDoubleSpinBox(self.filterOperation_tab)
        self.filterStart_doubleSpinBox.setObjectName(u"filterStart_doubleSpinBox")
        sizePolicy2.setHeightForWidth(self.filterStart_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.filterStart_doubleSpinBox.setSizePolicy(sizePolicy2)
        self.filterStart_doubleSpinBox.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.filterStart_doubleSpinBox.setKeyboardTracking(False)
        self.filterStart_doubleSpinBox.setMinimum(-10000000.000000000000000)
        self.filterStart_doubleSpinBox.setMaximum(10000000.000000000000000)

        self.gridLayout.addWidget(self.filterStart_doubleSpinBox, 2, 1, 1, 1)

        self.filterEndBelongTo_comboBox = QComboBox(self.filterOperation_tab)
        self.filterEndBelongTo_comboBox.addItem("")
        self.filterEndBelongTo_comboBox.addItem("")
        self.filterEndBelongTo_comboBox.setObjectName(u"filterEndBelongTo_comboBox")

        self.gridLayout.addWidget(self.filterEndBelongTo_comboBox, 2, 5, 1, 1)

        self.label = QLabel(self.filterOperation_tab)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 7)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.filterOperation_tab, "")
        self.interpolationOperation_tab = QWidget()
        self.interpolationOperation_tab.setObjectName(u"interpolationOperation_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.interpolationOperation_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.interpolationOperation_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 3)

        self.label_8 = QLabel(self.interpolationOperation_tab)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_6 = QLabel(self.interpolationOperation_tab)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)

        self.interpolationNumberOfPoints_spinBox = QSpinBox(self.interpolationOperation_tab)
        self.interpolationNumberOfPoints_spinBox.setObjectName(u"interpolationNumberOfPoints_spinBox")
        sizePolicy2.setHeightForWidth(self.interpolationNumberOfPoints_spinBox.sizePolicy().hasHeightForWidth())
        self.interpolationNumberOfPoints_spinBox.setSizePolicy(sizePolicy2)
        self.interpolationNumberOfPoints_spinBox.setKeyboardTracking(False)
        self.interpolationNumberOfPoints_spinBox.setMaximum(10000000)

        self.gridLayout_2.addWidget(self.interpolationNumberOfPoints_spinBox, 2, 1, 1, 1)

        self.interpolationType_comboBox = QComboBox(self.interpolationOperation_tab)
        self.interpolationType_comboBox.addItem("")
        self.interpolationType_comboBox.addItem("")
        self.interpolationType_comboBox.addItem("")
        self.interpolationType_comboBox.setObjectName(u"interpolationType_comboBox")
        sizePolicy2.setHeightForWidth(self.interpolationType_comboBox.sizePolicy().hasHeightForWidth())
        self.interpolationType_comboBox.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.interpolationType_comboBox, 2, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.interpolationOperation_tab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.makeOperation_pushButton = QPushButton(self.groupBox)
        self.makeOperation_pushButton.setObjectName(u"makeOperation_pushButton")

        self.verticalLayout_5.addWidget(self.makeOperation_pushButton)


        self.gridLayout_4.addWidget(self.groupBox, 2, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(dataTransformationToolbox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.variableInput_comboBox = QComboBox(dataTransformationToolbox)
        self.variableInput_comboBox.setObjectName(u"variableInput_comboBox")

        self.verticalLayout_2.addWidget(self.variableInput_comboBox)

        self.variableInput_parameterTree = ParameterTree(dataTransformationToolbox)
        self.variableInput_parameterTree.setObjectName(u"variableInput_parameterTree")

        self.verticalLayout_2.addWidget(self.variableInput_parameterTree)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(dataTransformationToolbox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.variableOutput_parameterTree = ParameterTree(dataTransformationToolbox)
        self.variableOutput_parameterTree.setObjectName(u"variableOutput_parameterTree")

        self.verticalLayout.addWidget(self.variableOutput_parameterTree)

        self.storeVariableOutput_pushButton = QPushButton(dataTransformationToolbox)
        self.storeVariableOutput_pushButton.setObjectName(u"storeVariableOutput_pushButton")

        self.verticalLayout.addWidget(self.storeVariableOutput_pushButton)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_21 = QLabel(dataTransformationToolbox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_21)

        self.operationList_parameterTree = ParameterTree(dataTransformationToolbox)
        self.operationList_parameterTree.setObjectName(u"operationList_parameterTree")

        self.verticalLayout_3.addWidget(self.operationList_parameterTree)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.operactionActionUp_pushButton = QPushButton(dataTransformationToolbox)
        self.operactionActionUp_pushButton.setObjectName(u"operactionActionUp_pushButton")

        self.horizontalLayout_2.addWidget(self.operactionActionUp_pushButton)

        self.operactionActionDown_pushButton = QPushButton(dataTransformationToolbox)
        self.operactionActionDown_pushButton.setObjectName(u"operactionActionDown_pushButton")

        self.horizontalLayout_2.addWidget(self.operactionActionDown_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.saveOperationList_pushButton = QPushButton(dataTransformationToolbox)
        self.saveOperationList_pushButton.setObjectName(u"saveOperationList_pushButton")

        self.horizontalLayout.addWidget(self.saveOperationList_pushButton)

        self.refreshOperationList_pushButton = QPushButton(dataTransformationToolbox)
        self.refreshOperationList_pushButton.setObjectName(u"refreshOperationList_pushButton")

        self.horizontalLayout.addWidget(self.refreshOperationList_pushButton)

        self.operationList_toolButton = QToolButton(dataTransformationToolbox)
        self.operationList_toolButton.setObjectName(u"operationList_toolButton")

        self.horizontalLayout.addWidget(self.operationList_toolButton)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_4)

        QWidget.setTabOrder(self.variableInput_comboBox, self.refreshOperationList_pushButton)
        QWidget.setTabOrder(self.refreshOperationList_pushButton, self.saveOperationList_pushButton)
        QWidget.setTabOrder(self.saveOperationList_pushButton, self.operationList_toolButton)
        QWidget.setTabOrder(self.operationList_toolButton, self.storeVariableOutput_pushButton)
        QWidget.setTabOrder(self.storeVariableOutput_pushButton, self.basicOperationChoice_comboBox)
        QWidget.setTabOrder(self.basicOperationChoice_comboBox, self.basicOperationPredef_comboBox)
        QWidget.setTabOrder(self.basicOperationPredef_comboBox, self.basicOperation_doubleSpinBox)
        QWidget.setTabOrder(self.basicOperation_doubleSpinBox, self.filterStart_doubleSpinBox)
        QWidget.setTabOrder(self.filterStart_doubleSpinBox, self.filterEnd__doubleSpinBox)
        QWidget.setTabOrder(self.filterEnd__doubleSpinBox, self.interpolationType_comboBox)
        QWidget.setTabOrder(self.interpolationType_comboBox, self.interpolationNumberOfPoints_spinBox)

        self.retranslateUi(dataTransformationToolbox)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dataTransformationToolbox)
    # setupUi

    def retranslateUi(self, dataTransformationToolbox):
        dataTransformationToolbox.setWindowTitle(QCoreApplication.translate("dataTransformationToolbox", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("dataTransformationToolbox", u"Operation", None))
        self.basicOperationPredef_comboBox.setItemText(0, QCoreApplication.translate("dataTransformationToolbox", u"Mean value", None))
        self.basicOperationPredef_comboBox.setItemText(1, QCoreApplication.translate("dataTransformationToolbox", u"First value", None))
        self.basicOperationPredef_comboBox.setItemText(2, QCoreApplication.translate("dataTransformationToolbox", u"End value", None))
        self.basicOperationPredef_comboBox.setItemText(3, QCoreApplication.translate("dataTransformationToolbox", u"Min value", None))
        self.basicOperationPredef_comboBox.setItemText(4, QCoreApplication.translate("dataTransformationToolbox", u"Custom value", None))

        self.basicOperationChoice_comboBox.setItemText(0, QCoreApplication.translate("dataTransformationToolbox", u"Add", None))
        self.basicOperationChoice_comboBox.setItemText(1, QCoreApplication.translate("dataTransformationToolbox", u"Substract", None))
        self.basicOperationChoice_comboBox.setItemText(2, QCoreApplication.translate("dataTransformationToolbox", u"Multiply", None))
        self.basicOperationChoice_comboBox.setItemText(3, QCoreApplication.translate("dataTransformationToolbox", u"Divide", None))

        self.label_20.setText(QCoreApplication.translate("dataTransformationToolbox", u"Basic Operation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basicOperation_tab), QCoreApplication.translate("dataTransformationToolbox", u"Basic", None))
        self.label_10.setText(QCoreApplication.translate("dataTransformationToolbox", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("dataTransformationToolbox", u"Start", None))
        self.filterStartBelongTo_comboBox.setItemText(0, QCoreApplication.translate("dataTransformationToolbox", u"In", None))
        self.filterStartBelongTo_comboBox.setItemText(1, QCoreApplication.translate("dataTransformationToolbox", u"Out", None))

        self.filterFlip_comboBox.setItemText(0, QCoreApplication.translate("dataTransformationToolbox", u"Within edges", None))
        self.filterFlip_comboBox.setItemText(1, QCoreApplication.translate("dataTransformationToolbox", u"Outside edges", None))

        self.label_7.setText(QCoreApplication.translate("dataTransformationToolbox", u"End", None))
        self.label_2.setText(QCoreApplication.translate("dataTransformationToolbox", u"-", None))
        self.filterStart_doubleSpinBox.setPrefix("")
        self.filterStart_doubleSpinBox.setSuffix("")
        self.filterEndBelongTo_comboBox.setItemText(0, QCoreApplication.translate("dataTransformationToolbox", u"In", None))
        self.filterEndBelongTo_comboBox.setItemText(1, QCoreApplication.translate("dataTransformationToolbox", u"Out", None))

        self.label.setText(QCoreApplication.translate("dataTransformationToolbox", u"Filter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filterOperation_tab), QCoreApplication.translate("dataTransformationToolbox", u"Filter", None))
        self.label_3.setText(QCoreApplication.translate("dataTransformationToolbox", u"Interpolation", None))
        self.label_8.setText(QCoreApplication.translate("dataTransformationToolbox", u"Type", None))
        self.label_6.setText(QCoreApplication.translate("dataTransformationToolbox", u"Number of points", None))
        self.interpolationType_comboBox.setItemText(0, QCoreApplication.translate("dataTransformationToolbox", u"Linear", None))
        self.interpolationType_comboBox.setItemText(1, QCoreApplication.translate("dataTransformationToolbox", u"Cubic", None))
        self.interpolationType_comboBox.setItemText(2, QCoreApplication.translate("dataTransformationToolbox", u"Custom axis", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.interpolationOperation_tab), QCoreApplication.translate("dataTransformationToolbox", u"Interpolation", None))
        self.makeOperation_pushButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"Apply", None))
        self.label_5.setText(QCoreApplication.translate("dataTransformationToolbox", u"Variable input", None))
        self.label_9.setText(QCoreApplication.translate("dataTransformationToolbox", u"Variable output", None))
        self.storeVariableOutput_pushButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"Store", None))
        self.label_21.setText(QCoreApplication.translate("dataTransformationToolbox", u"List of operations", None))
        self.operactionActionUp_pushButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"+", None))
        self.operactionActionDown_pushButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"-", None))
        self.saveOperationList_pushButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"Save", None))
        self.refreshOperationList_pushButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"Refresh", None))
        self.operationList_toolButton.setText(QCoreApplication.translate("dataTransformationToolbox", u"...", None))
    # retranslateUi

