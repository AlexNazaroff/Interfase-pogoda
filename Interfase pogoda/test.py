# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pogoda.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(381, 279)
        Dialog.setStyleSheet(u"background-color: #1d1c21;")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 60, 141, 31))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: #f2b824;\n"
"	font: 18pt \"Century\";\n"
"background-color: #1d1c21;\n"
"border: none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: #f2c44e;\n"
"\n"
"background-color: #3a3c42;\n"
"}\n"
"QPushButton:pressed{\n"
"color: #eb7b13;\n"
"\n"
"\n"
"background-color: #3a3c42;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 90, 211, 141))
        self.label.setStyleSheet(u"color: #ccc;\n"
"	font: 18pt \"Century\";")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 20, 221, 31))
        self.lineEdit.setStyleSheet(u"color: #e0bd3f;\n"
"font: 20pt \"DaunPenh\";\n"
"background-color: #1d1c21;\n"
"border: none;")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
        self.label.setText("")
        self.lineEdit.setText("")
    # retranslateUi

