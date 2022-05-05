# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advancedPlot_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

from pyqtgraph import GraphicsLayoutWidget

class Ui_advancedPlot_panel(object):
    def setupUi(self, advancedPlot_panel):
        if not advancedPlot_panel.objectName():
            advancedPlot_panel.setObjectName(u"advancedPlot_panel")
        advancedPlot_panel.resize(652, 560)
        self.verticalLayout_3 = QVBoxLayout(advancedPlot_panel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.makePlot_toolButton = QToolButton(advancedPlot_panel)
        self.makePlot_toolButton.setObjectName(u"makePlot_toolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makePlot_toolButton.sizePolicy().hasHeightForWidth())
        self.makePlot_toolButton.setSizePolicy(sizePolicy)
        self.makePlot_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.makePlot_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.makePlot_toolButton.setAutoRaise(False)
        self.makePlot_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.makePlot_toolButton)

        self.checkBox = QCheckBox(advancedPlot_panel)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.plot_listWidget = QListWidget(advancedPlot_panel)
        self.plot_listWidget.setObjectName(u"plot_listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plot_listWidget.sizePolicy().hasHeightForWidth())
        self.plot_listWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.plot_listWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.makeROI_toolButton = QToolButton(advancedPlot_panel)
        self.makeROI_toolButton.setObjectName(u"makeROI_toolButton")
        sizePolicy.setHeightForWidth(self.makeROI_toolButton.sizePolicy().hasHeightForWidth())
        self.makeROI_toolButton.setSizePolicy(sizePolicy)
        self.makeROI_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.makeROI_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.makeROI_toolButton.setAutoRaise(False)
        self.makeROI_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_2.addWidget(self.makeROI_toolButton)

        self.ROI_listWidget = QListWidget(advancedPlot_panel)
        self.ROI_listWidget.setObjectName(u"ROI_listWidget")
        sizePolicy1.setHeightForWidth(self.ROI_listWidget.sizePolicy().hasHeightForWidth())
        self.ROI_listWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.ROI_listWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.plot_graphicsView = GraphicsLayoutWidget(advancedPlot_panel)
        self.plot_graphicsView.setObjectName(u"plot_graphicsView")

        self.verticalLayout_3.addWidget(self.plot_graphicsView)


        self.retranslateUi(advancedPlot_panel)

        QMetaObject.connectSlotsByName(advancedPlot_panel)
    # setupUi

    def retranslateUi(self, advancedPlot_panel):
        advancedPlot_panel.setWindowTitle(QCoreApplication.translate("advancedPlot_panel", u"Form", None))
        self.makePlot_toolButton.setText(QCoreApplication.translate("advancedPlot_panel", u"Add Plot", None))
        self.checkBox.setText(QCoreApplication.translate("advancedPlot_panel", u"Normalize plots", None))
        self.makeROI_toolButton.setText(QCoreApplication.translate("advancedPlot_panel", u"Add ROI", None))
    # retranslateUi

