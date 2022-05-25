# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration_parameters.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Calibration_parameters(object):
    def setupUi(self, Calibration_parameters):
        if not Calibration_parameters.objectName():
            Calibration_parameters.setObjectName(u"Calibration_parameters")
        Calibration_parameters.setEnabled(True)
        Calibration_parameters.resize(455, 225)
        self.horizontalLayout = QHBoxLayout(Calibration_parameters)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(1, -1, -1, -1)
        self.label_4 = QLabel(Calibration_parameters)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.vertical_layout.addWidget(self.label_4)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.label = QLabel(Calibration_parameters)
        self.label.setObjectName(u"label")

        self.horizontal_layout.addWidget(self.label)

        self.inputAxis0Mult_lineEdit_2 = QLineEdit(Calibration_parameters)
        self.inputAxis0Mult_lineEdit_2.setObjectName(u"inputAxis0Mult_lineEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputAxis0Mult_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.inputAxis0Mult_lineEdit_2.setSizePolicy(sizePolicy1)

        self.horizontal_layout.addWidget(self.inputAxis0Mult_lineEdit_2)


        self.vertical_layout.addLayout(self.horizontal_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Calibration_parameters)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.inputAxis0Mult_lineEdit = QLineEdit(Calibration_parameters)
        self.inputAxis0Mult_lineEdit.setObjectName(u"inputAxis0Mult_lineEdit")
        sizePolicy1.setHeightForWidth(self.inputAxis0Mult_lineEdit.sizePolicy().hasHeightForWidth())
        self.inputAxis0Mult_lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.inputAxis0Mult_lineEdit)


        self.vertical_layout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Calibration_parameters)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.inputAxis0Mult_lineEdit_3 = QLineEdit(Calibration_parameters)
        self.inputAxis0Mult_lineEdit_3.setObjectName(u"inputAxis0Mult_lineEdit_3")
        sizePolicy1.setHeightForWidth(self.inputAxis0Mult_lineEdit_3.sizePolicy().hasHeightForWidth())
        self.inputAxis0Mult_lineEdit_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.inputAxis0Mult_lineEdit_3)


        self.vertical_layout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.vertical_layout)


        self.retranslateUi(Calibration_parameters)

        QMetaObject.connectSlotsByName(Calibration_parameters)
    # setupUi

    def retranslateUi(self, Calibration_parameters):
        Calibration_parameters.setWindowTitle(QCoreApplication.translate("Calibration_parameters", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Calibration_parameters", u"Peak finder parameters", None))
        self.label.setText(QCoreApplication.translate("Calibration_parameters", u"Prominence factor", None))
        self.inputAxis0Mult_lineEdit_2.setText(QCoreApplication.translate("Calibration_parameters", u"0.05", None))
        self.label_2.setText(QCoreApplication.translate("Calibration_parameters", u"Distance between peaks", None))
        self.inputAxis0Mult_lineEdit.setText(QCoreApplication.translate("Calibration_parameters", u"100", None))
        self.label_3.setText(QCoreApplication.translate("Calibration_parameters", u"Relative height of peaks", None))
        self.inputAxis0Mult_lineEdit_3.setText(QCoreApplication.translate("Calibration_parameters", u"0.5", None))
    # retranslateUi

