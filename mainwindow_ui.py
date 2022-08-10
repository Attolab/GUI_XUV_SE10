# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 328)
        MainWindow.setDockNestingEnabled(True)
        self.menuFile_restartAction = QAction(MainWindow)
        self.menuFile_restartAction.setObjectName(u"menuFile_restartAction")
        self.quit_action = QAction(MainWindow)
        self.quit_action.setObjectName(u"quit_action")
        self.restart_action = QAction(MainWindow)
        self.restart_action.setObjectName(u"restart_action")
        self.actiong = QAction(MainWindow)
        self.actiong.setObjectName(u"actiong")
        self.load_action = QAction(MainWindow)
        self.load_action.setObjectName(u"load_action")
        self.restoreState_action = QAction(MainWindow)
        self.restoreState_action.setObjectName(u"restoreState_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 491, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.load_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.restart_action)
        self.menuFile.addAction(self.quit_action)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.restoreState_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuFile_restartAction.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.quit_action.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.restart_action.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.actiong.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.load_action.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.restoreState_action.setText(QCoreApplication.translate("MainWindow", u"Restore initial state", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

