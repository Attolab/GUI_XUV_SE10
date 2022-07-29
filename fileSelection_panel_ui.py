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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_FileSelectionPanel(object):
    def setupUi(self, FileSelectionPanel):
        if not FileSelectionPanel.objectName():
            FileSelectionPanel.setObjectName(u"FileSelectionPanel")
        FileSelectionPanel.resize(274, 371)
        self.actionAddEntry = QAction(FileSelectionPanel)
        self.actionAddEntry.setObjectName(u"actionAddEntry")
        self.verticalLayout = QVBoxLayout(FileSelectionPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileSelection_listWidget = QListWidget(FileSelectionPanel)
        self.fileSelection_listWidget.setObjectName(u"fileSelection_listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
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


        self.retranslateUi(FileSelectionPanel)

        QMetaObject.connectSlotsByName(FileSelectionPanel)
    # setupUi

    def retranslateUi(self, FileSelectionPanel):
        FileSelectionPanel.setWindowTitle(QCoreApplication.translate("FileSelectionPanel", u"Form", None))
        self.actionAddEntry.setText(QCoreApplication.translate("FileSelectionPanel", u"Add Entry", None))
        self.makeInput_pushButton.setText(QCoreApplication.translate("FileSelectionPanel", u"Make", None))
    # retranslateUi

