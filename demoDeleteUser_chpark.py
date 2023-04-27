# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoDeleteUser_chpark.ui'
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
        self.label.setGeometry(QRect(50, 30, 171, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 161, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 140, 181, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 190, 181, 22))
        self.labelSure = QLabel(Dialog)
        self.labelSure.setObjectName(u"labelSure")
        self.labelSure.setGeometry(QRect(90, 320, 161, 22))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(50, 400, 501, 22))
        self.lineEditDBName = QLineEdit(Dialog)
        self.lineEditDBName.setObjectName(u"lineEditDBName")
        self.lineEditDBName.setGeometry(QRect(260, 30, 231, 32))
        self.lineEditDBName.setStyleSheet(u"background-color: white")
        self.lineEditTableName = QLineEdit(Dialog)
        self.lineEditTableName.setObjectName(u"lineEditTableName")
        self.lineEditTableName.setGeometry(QRect(260, 70, 231, 32))
        self.lineEditTableName.setStyleSheet(u"background-color: white")
        self.lineEditEmailAddress = QLineEdit(Dialog)
        self.lineEditEmailAddress.setObjectName(u"lineEditEmailAddress")
        self.lineEditEmailAddress.setGeometry(QRect(260, 140, 231, 32))
        self.lineEditEmailAddress.setStyleSheet(u"background-color: white")
        self.lineEditPassword = QLineEdit(Dialog)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(260, 180, 231, 32))
        self.lineEditPassword.setStyleSheet(u"background-color: white")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.pushButtonDelete = QPushButton(Dialog)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setGeometry(QRect(220, 240, 151, 30))
        self.pushButtonYes = QPushButton(Dialog)
        self.pushButtonYes.setObjectName(u"pushButtonYes")
        self.pushButtonYes.setGeometry(QRect(270, 320, 91, 30))
        self.pushButtonNo = QPushButton(Dialog)
        self.pushButtonNo.setObjectName(u"pushButtonNo")
        self.pushButtonNo.setGeometry(QRect(410, 320, 91, 30))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 0, 391, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter database name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter table name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Email Address</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Password</span></p></body></html>", None))
        self.labelSure.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Are you Sure ?</span></p></body></html>", None))
        self.labelResponse.setText("")
        self.pushButtonDelete.setText(QCoreApplication.translate("Dialog", u"Delete User", None))
        self.pushButtonYes.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.pushButtonNo.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">2020041091-3-3-chpark-embeddedsoftware-midTerm</span></p></body></html>", None))
    # retranslateUi

