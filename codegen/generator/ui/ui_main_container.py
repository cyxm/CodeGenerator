# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_container.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from codegen.generator.ui.widget.container.ui_widget_main_container import Ui_ContainerMain
from codegen.generator.ui.widget.func.ui_widget_title import Ui_Widget_Title


class UiMainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("CodeGeneratorKits")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        # MainWindow.resize(800, 600)
        main_window.setStyleSheet("")
        main_window.setUnifiedTitleAndToolBarOnMac(False)

        p = main_window.takeCentralWidget()
        del p

        #
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
