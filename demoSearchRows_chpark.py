# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoSearchRows_chpark.ui'
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
        Dialog.resize(600, 480)
        Dialog.setStyleSheet(u"background-color: rgb(165, 255, 214)")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 201, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 100, 201, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 210, 241, 22))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(40, 320, 511, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 400, 191, 22))
        self.pushButtonSearch = QPushButton(Dialog)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")
        self.pushButtonSearch.setGeometry(QRect(220, 250, 99, 30))
        self.lineEditDBName = QLineEdit(Dialog)
        self.lineEditDBName.setObjectName(u"lineEditDBName")
        self.lineEditDBName.setGeometry(QRect(260, 50, 221, 32))
        self.lineEditDBName.setStyleSheet(u"background-color: white")
        self.lineEditTableName = QLineEdit(Dialog)
        self.lineEditTableName.setObjectName(u"lineEditTableName")
        self.lineEditTableName.setGeometry(QRect(260, 100, 221, 32))
        self.lineEditTableName.setStyleSheet(u"background-color: white")
        self.lineEditEmailAddress = QLineEdit(Dialog)
        self.lineEditEmailAddress.setObjectName(u"lineEditEmailAddress")
        self.lineEditEmailAddress.setGeometry(QRect(280, 200, 271, 32))
        self.lineEditEmailAddress.setStyleSheet(u"background-color: white")
        self.lineEditPassword = QLineEdit(Dialog)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(260, 400, 221, 32))
        self.lineEditPassword.setStyleSheet(u"background-color: white")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 10, 391, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter database name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter table name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Email Address(FOR WHERE LIKE)</span></p></body></html>", None))
        self.labelResponse.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Password(Result Record)</span></p></body></html>", None))
        self.pushButtonSearch.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">2020041091-3-2-chpark-embeddedsoftware-midterm</span></p></body></html>", None))
    # retranslateUi

