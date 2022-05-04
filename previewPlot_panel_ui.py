# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'previewPlot_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_previewPlot_Panel(object):
    def setupUi(self, previewPlot_Panel):
        if not previewPlot_Panel.objectName():
            previewPlot_Panel.setObjectName(u"previewPlot_Panel")
        previewPlot_Panel.resize(799, 660)
        self.verticalLayout_2 = QVBoxLayout(previewPlot_Panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.signalInput_groupBox = QGroupBox(previewPlot_Panel)
        self.signalInput_groupBox.setObjectName(u"signalInput_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalInput_groupBox.sizePolicy().hasHeightForWidth())
        self.signalInput_groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.signalInput_groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_2.addWidget(self.signalInput_groupBox)

        self.signalOutput_groupBox = QGroupBox(previewPlot_Panel)
        self.signalOutput_groupBox.setObjectName(u"signalOutput_groupBox")
        sizePolicy.setHeightForWidth(self.signalOutput_groupBox.sizePolicy().hasHeightForWidth())
        self.signalOutput_groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.signalOutput_groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_2.addWidget(self.signalOutput_groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.signal_checkBox = QCheckBox(previewPlot_Panel)
        self.signal_checkBox.setObjectName(u"signal_checkBox")
        self.signal_checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.signal_checkBox)

        self.FT_magn_checkBox = QCheckBox(previewPlot_Panel)
        self.FT_magn_checkBox.setObjectName(u"FT_magn_checkBox")
        self.FT_magn_checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.FT_magn_checkBox)

        self.FT_phase_checkBox = QCheckBox(previewPlot_Panel)
        self.FT_phase_checkBox.setObjectName(u"FT_phase_checkBox")
        self.FT_phase_checkBox.setChecked(False)

        self.horizontalLayout.addWidget(self.FT_phase_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.configuration_button = QPushButton(previewPlot_Panel)
        self.configuration_button.setObjectName(u"configuration_button")

        self.verticalLayout.addWidget(self.configuration_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(previewPlot_Panel)

        QMetaObject.connectSlotsByName(previewPlot_Panel)
    # setupUi

    def retranslateUi(self, previewPlot_Panel):
        previewPlot_Panel.setWindowTitle(QCoreApplication.translate("previewPlot_Panel", u"Form", None))
        self.signalInput_groupBox.setTitle(QCoreApplication.translate("previewPlot_Panel", u"Signal", None))
        self.signalOutput_groupBox.setTitle(QCoreApplication.translate("previewPlot_Panel", u"Fourier transform", None))
        self.signal_checkBox.setText(QCoreApplication.translate("previewPlot_Panel", u"Show Signal", None))
        self.FT_magn_checkBox.setText(QCoreApplication.translate("previewPlot_Panel", u"Show Magn", None))
        self.FT_phase_checkBox.setText(QCoreApplication.translate("previewPlot_Panel", u"Show Phase", None))
        self.configuration_button.setText(QCoreApplication.translate("previewPlot_Panel", u"Configuration", None))
    # retranslateUi

