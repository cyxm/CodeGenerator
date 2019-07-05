# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_container.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from generator.ui.widget.container.ui_widget_main_container import Ui_ContainerMain
from generator.ui.widget.func.ui_widget_title import Ui_Widget_Title


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        # MainWindow.resize(800, 618)
        MainWindow.setStyleSheet("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        # 设置主内容控件
        centralWidget = QtWidgets.QWidget()
        ui = Ui_ContainerMain()
        ui.setupUi(centralWidget)
        MainWindow.setCentralWidget(centralWidget)
        verticalLayout = QtWidgets.QVBoxLayout(centralWidget)

        #
        title = QtWidgets.QWidget()
        ui = Ui_Widget_Title()
        ui.setupUi(title)
        verticalLayout.addWidget(title)

        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
