# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_6 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_6.setMinimumSize(QtCore.QSize(200, 38))
        self.dockWidget_6.setMaximumSize(QtCore.QSize(500, 524287))
        self.dockWidget_6.setFloating(False)
        self.dockWidget_6.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_6.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_6.setWindowTitle("")
        self.dockWidget_6.setObjectName("dockWidget_6")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.dockWidget_6.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_6)
        self.dockWidget_13 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_13.setObjectName("dockWidget_13")
        self.dockWidgetContents_13 = QtWidgets.QWidget()
        self.dockWidgetContents_13.setObjectName("dockWidgetContents_13")
        self.dockWidget_13.setWidget(self.dockWidgetContents_13)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_13)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

