# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer1D_widget.ui'
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
    QHBoxLayout, QHeaderView, QLayout, QPushButton,
    QSizePolicy, QSplitter, QTableWidgetItem, QToolBox,
    QToolButton, QVBoxLayout, QWidget)

from CustomTableWidget import (PlotTableWidget, ROITableWidget)
from ParameterTree import CustomParameterTree
from pyqtgraph import GraphicsLayoutWidget

class Ui_Viewer1DWidget(object):
    def setupUi(self, Viewer1DWidget):
        if not Viewer1DWidget.objectName():
            Viewer1DWidget.setObjectName(u"Viewer1DWidget")
        Viewer1DWidget.resize(795, 443)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Viewer1DWidget.sizePolicy().hasHeightForWidth())
        Viewer1DWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Viewer1DWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(Viewer1DWidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setFrameShadow(QFrame.Plain)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(True)
        self.viewer_GraphicsLayoutWidget = GraphicsLayoutWidget(self.splitter)
        self.viewer_GraphicsLayoutWidget.setObjectName(u"viewer_GraphicsLayoutWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.viewer_GraphicsLayoutWidget.sizePolicy().hasHeightForWidth())
        self.viewer_GraphicsLayoutWidget.setSizePolicy(sizePolicy2)
        self.splitter.addWidget(self.viewer_GraphicsLayoutWidget)
        self.toolBox = QToolBox(self.splitter)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QSize(50, 0))
        self.toolBox.setFrameShape(QFrame.Panel)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 274, 361))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy3)
        self.page.setMinimumSize(QSize(40, 0))
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.tablePlot_tableWidget = PlotTableWidget(self.page)
        if (self.tablePlot_tableWidget.columnCount() < 3):
            self.tablePlot_tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePlot_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePlot_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePlot_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tablePlot_tableWidget.setObjectName(u"tablePlot_tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tablePlot_tableWidget.sizePolicy().hasHeightForWidth())
        self.tablePlot_tableWidget.setSizePolicy(sizePolicy4)
        self.tablePlot_tableWidget.setMinimumSize(QSize(0, 0))
        self.tablePlot_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePlot_tableWidget.horizontalHeader().setHighlightSections(False)
        self.tablePlot_tableWidget.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tablePlot_tableWidget)

        self.plot_ParameterTree = CustomParameterTree(self.page)
        self.plot_ParameterTree.setObjectName(u"plot_ParameterTree")

        self.verticalLayout.addWidget(self.plot_ParameterTree)

        self.addPlot_pushButton = QPushButton(self.page)
        self.addPlot_pushButton.setObjectName(u"addPlot_pushButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.addPlot_pushButton.sizePolicy().hasHeightForWidth())
        self.addPlot_pushButton.setSizePolicy(sizePolicy5)

        self.verticalLayout.addWidget(self.addPlot_pushButton)

        self.toolBox.addItem(self.page, u"Display")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 399, 361))
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.showROI_checkBox = QCheckBox(self.page_2)
        self.showROI_checkBox.setObjectName(u"showROI_checkBox")
        self.showROI_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.showROI_checkBox)

        self.makeROI_toolButton = QToolButton(self.page_2)
        self.makeROI_toolButton.setObjectName(u"makeROI_toolButton")
        sizePolicy5.setHeightForWidth(self.makeROI_toolButton.sizePolicy().hasHeightForWidth())
        self.makeROI_toolButton.setSizePolicy(sizePolicy5)
        self.makeROI_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.makeROI_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.makeROI_toolButton.setAutoRaise(False)
        self.makeROI_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_2.addWidget(self.makeROI_toolButton)

        self.makeIL_toolButton = QToolButton(self.page_2)
        self.makeIL_toolButton.setObjectName(u"makeIL_toolButton")
        sizePolicy5.setHeightForWidth(self.makeIL_toolButton.sizePolicy().hasHeightForWidth())
        self.makeIL_toolButton.setSizePolicy(sizePolicy5)
        self.makeIL_toolButton.setPopupMode(QToolButton.MenuButtonPopup)
        self.makeIL_toolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.makeIL_toolButton.setAutoRaise(False)
        self.makeIL_toolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_2.addWidget(self.makeIL_toolButton)

        self.tableROI_tableWidget = ROITableWidget(self.page_2)
        if (self.tableROI_tableWidget.columnCount() < 3):
            self.tableROI_tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableROI_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableROI_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableROI_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableROI_tableWidget.setObjectName(u"tableROI_tableWidget")
        sizePolicy4.setHeightForWidth(self.tableROI_tableWidget.sizePolicy().hasHeightForWidth())
        self.tableROI_tableWidget.setSizePolicy(sizePolicy4)
        self.tableROI_tableWidget.setMinimumSize(QSize(0, 0))
        self.tableROI_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableROI_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableROI_tableWidget)

        self.toolBox.addItem(self.page_2, u"ROI")
        self.splitter.addWidget(self.toolBox)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(Viewer1DWidget)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(Viewer1DWidget)
    # setupUi

    def retranslateUi(self, Viewer1DWidget):
        Viewer1DWidget.setWindowTitle(QCoreApplication.translate("Viewer1DWidget", u"Form", None))
        ___qtablewidgetitem = self.tablePlot_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Viewer1DWidget", u"Name", None));
        ___qtablewidgetitem1 = self.tablePlot_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Viewer1DWidget", u"Color", None));
        ___qtablewidgetitem2 = self.tablePlot_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Viewer1DWidget", u"Show", None));
        self.addPlot_pushButton.setText(QCoreApplication.translate("Viewer1DWidget", u"AddPlot", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Viewer1DWidget", u"Display", None))
        self.showROI_checkBox.setText(QCoreApplication.translate("Viewer1DWidget", u"ROI", None))
        self.makeROI_toolButton.setText(QCoreApplication.translate("Viewer1DWidget", u"Add ROI", None))
        self.makeIL_toolButton.setText(QCoreApplication.translate("Viewer1DWidget", u"Add ROI", None))
        ___qtablewidgetitem3 = self.tableROI_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Viewer1DWidget", u"Name", None));
        ___qtablewidgetitem4 = self.tableROI_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Viewer1DWidget", u"Orientation", None));
        ___qtablewidgetitem5 = self.tableROI_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Viewer1DWidget", u"Type", None));
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Viewer1DWidget", u"ROI", None))
    # retranslateUi

