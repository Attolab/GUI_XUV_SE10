# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileSelection_panel.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph.parametertree import ParameterTree

class Ui_FileSelectionPanel(object):
    def setupUi(self, FileSelectionPanel):
        if not FileSelectionPanel.objectName():
            FileSelectionPanel.setObjectName(u"FileSelectionPanel")
        FileSelectionPanel.resize(705, 532)
        FileSelectionPanel.setLocale(QLocale(QLocale.C, QLocale.AnyTerritory))
        self.actionAddEntry = QAction(FileSelectionPanel)
        self.actionAddEntry.setObjectName(u"actionAddEntry")
        self.verticalLayout = QVBoxLayout(FileSelectionPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileSelection_listWidget = QListWidget(FileSelectionPanel)
        self.fileSelection_listWidget.setObjectName(u"fileSelection_listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileSelection_listWidget.sizePolicy().hasHeightForWidth())
        self.fileSelection_listWidget.setSizePolicy(sizePolicy)
        self.fileSelection_listWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.fileSelection_listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.fileSelection_listWidget.setDefaultDropAction(Qt.MoveAction)
        self.fileSelection_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.fileSelection_listWidget.setMovement(QListView.Free)

        self.verticalLayout.addWidget(self.fileSelection_listWidget)

        self.makeInput_pushButton = QPushButton(FileSelectionPanel)
        self.makeInput_pushButton.setObjectName(u"makeInput_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.makeInput_pushButton.sizePolicy().hasHeightForWidth())
        self.makeInput_pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.makeInput_pushButton)

        self.showDetails_checkBox = QCheckBox(FileSelectionPanel)
        self.showDetails_checkBox.setObjectName(u"showDetails_checkBox")
        self.showDetails_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.showDetails_checkBox)

        self.fileDetails_tabwidget = QTabWidget(FileSelectionPanel)
        self.fileDetails_tabwidget.setObjectName(u"fileDetails_tabwidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fileDetails_tabwidget.sizePolicy().hasHeightForWidth())
        self.fileDetails_tabwidget.setSizePolicy(sizePolicy2)
        self.fileDetails_tabwidget.setTabPosition(QTabWidget.North)
        self.fileDetails_tabwidget.setTabShape(QTabWidget.Rounded)
        self.fileDetails_tabwidget.setMovable(True)
        self.fileDes_parameterTree = ParameterTree()
        self.fileDes_parameterTree.setObjectName(u"fileDes_parameterTree")
        self.fileDetails_tabwidget.addTab(self.fileDes_parameterTree, "")
        self.fileAttr_parameterTree = ParameterTree()
        self.fileAttr_parameterTree.setObjectName(u"fileAttr_parameterTree")
        self.fileDetails_tabwidget.addTab(self.fileAttr_parameterTree, "")
        self.filePrev_parameterTree = ParameterTree()
        self.filePrev_parameterTree.setObjectName(u"filePrev_parameterTree")
        self.fileDetails_tabwidget.addTab(self.filePrev_parameterTree, "")

        self.verticalLayout.addWidget(self.fileDetails_tabwidget)


        self.retranslateUi(FileSelectionPanel)

        self.fileDetails_tabwidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(FileSelectionPanel)
    # setupUi

    def retranslateUi(self, FileSelectionPanel):
        FileSelectionPanel.setWindowTitle(QCoreApplication.translate("FileSelectionPanel", u"Form", None))
        self.actionAddEntry.setText(QCoreApplication.translate("FileSelectionPanel", u"Add Entry", None))
        self.makeInput_pushButton.setText(QCoreApplication.translate("FileSelectionPanel", u"Make", None))
        self.showDetails_checkBox.setText(QCoreApplication.translate("FileSelectionPanel", u"Show details", None))
        self.fileDetails_tabwidget.setTabText(self.fileDetails_tabwidget.indexOf(self.fileDes_parameterTree), QCoreApplication.translate("FileSelectionPanel", u"Description", None))
        self.fileDetails_tabwidget.setTabText(self.fileDetails_tabwidget.indexOf(self.fileAttr_parameterTree), QCoreApplication.translate("FileSelectionPanel", u"Attributes", None))
        self.fileDetails_tabwidget.setTabText(self.fileDetails_tabwidget.indexOf(self.filePrev_parameterTree), QCoreApplication.translate("FileSelectionPanel", u"Data", None))
    # retranslateUi

