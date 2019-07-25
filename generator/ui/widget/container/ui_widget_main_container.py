# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_widget_main_container.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ContainerMain(object):
    def setupUi(self, ContainerMain):
        ContainerMain.setObjectName("ContainerMain")
        ContainerMain.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ContainerMain.sizePolicy().hasHeightForWidth())
        ContainerMain.setSizePolicy(sizePolicy)

        self.retranslateUi(ContainerMain)
        QtCore.QMetaObject.connectSlotsByName(ContainerMain)

    def retranslateUi(self, ContainerMain):
        _translate = QtCore.QCoreApplication.translate
        ContainerMain.setWindowTitle(_translate("ContainerMain", "Form"))

