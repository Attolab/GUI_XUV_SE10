# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer2D_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QSizePolicy, QSplitter,
    QTableWidgetItem, QToolBox, QToolButton, QVBoxLayout,
    QWidget)

from CustomTableWidget import ROITableWidget
from pyqtgraph import GraphicsLayoutWidget

class Ui_Viewer2DWidget(object):
    def setupUi(self, Viewer2DWidget):
        if not Viewer2DWidget.objectName():
            Viewer2DWidget.setObjectName(u"Viewer2DWidget")
        Viewer2DWidget.resize(762, 443)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Viewer2DWidget.sizePolicy().hasHeightForWidth())
        Viewer2DWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Viewer2DWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(Viewer2DWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.viewer_GraphicsLayoutWidget = GraphicsLayoutWidget(self.splitter)
        self.viewer_GraphicsLayoutWidget.setObjectName(u"viewer_GraphicsLayoutWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewer_GraphicsLayoutWidget.sizePolicy().hasHeightForWidth())
        self.viewer_GraphicsLayoutWidget.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.viewer_GraphicsLayoutWidget)
        self.toolBox = QToolBox(self.splitter)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy2)
        self.toolBox.setMinimumSize(QSize(20, 0))
        self.toolBox.setFrameShape(QFrame.Panel)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 76, 361))
        sizePolicy2.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.show2D_checkBox = QCheckBox(self.page)
        self.show2D_checkBox.setObjectName(u"show2D_checkBox")
        self.show2D_checkBox.setChecked(True)
        self.show2D_checkBox.setTristate(False)

        self.verticalLayout.addWidget(self.show2D_checkBox)

        self.showHist_checkBox = QCheckBox(self.page)
        self.showHist_checkBox.setObjectName(u"showHist_checkBox")
        self.showHist_checkBox.setChecked(False)
        self.showHist_checkBox.setTristate(False)

        self.verticalLayout.addWidget(self.showHist_checkBox)

        self.showROI_checkBox = QCheckBox(self.page)
        self.showROI_checkBox.setObjectName(u"showROI_checkBox")
        self.showROI_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.showROI_checkBox)

        self.toolBox.addItem(self.page, u"Display")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 274, 361))
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.makeROI_toolButton = QToolButton(self.page_2)
        self.makeROI_toolButton.setObjectName(u"makeROI_toolButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.makeROI_toolButton.sizePolicy().hasHeightForWidth())
        self.makeROI_toolButton.setSizePolicy(sizePolicy3)
        self.makeROI_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.makeROI_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.makeROI_toolButton.setAutoRaise(False)
        self.makeROI_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_2.addWidget(self.makeROI_toolButton)

        self.tableROI_tableWidget = ROITableWidget(self.page_2)
        if (self.tableROI_tableWidget.columnCount() < 2):
            self.tableROI_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableROI_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableROI_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableROI_tableWidget.setObjectName(u"tableROI_tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableROI_tableWidget.sizePolicy().hasHeightForWidth())
        self.tableROI_tableWidget.setSizePolicy(sizePolicy4)
        self.tableROI_tableWidget.setMinimumSize(QSize(0, 0))
        self.tableROI_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableROI_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableROI_tableWidget)

        self.toolBox.addItem(self.page_2, u"ROI")
        self.splitter.addWidget(self.toolBox)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(Viewer2DWidget)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(Viewer2DWidget)
    # setupUi

    def retranslateUi(self, Viewer2DWidget):
        Viewer2DWidget.setWindowTitle(QCoreApplication.translate("Viewer2DWidget", u"Form", None))
        self.show2D_checkBox.setText(QCoreApplication.translate("Viewer2DWidget", u"Data", None))
        self.showHist_checkBox.setText(QCoreApplication.translate("Viewer2DWidget", u"Hist", None))
        self.showROI_checkBox.setText(QCoreApplication.translate("Viewer2DWidget", u"ROI", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Viewer2DWidget", u"Display", None))
        self.makeROI_toolButton.setText(QCoreApplication.translate("Viewer2DWidget", u"Add ROI", None))
        ___qtablewidgetitem = self.tableROI_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Viewer2DWidget", u"Name", None));
        ___qtablewidgetitem1 = self.tableROI_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Viewer2DWidget", u"Type", None));
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Viewer2DWidget", u"ROI", None))
    # retranslateUi

