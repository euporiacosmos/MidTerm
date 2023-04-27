# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoChangePassword_chpark.ui'
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
        self.label.setGeometry(QRect(40, 30, 181, 22))
        self.label.setStyleSheet(u"")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 181, 22))
        self.label_2.setStyleSheet(u"")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 150, 181, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 200, 181, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 250, 181, 22))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 310, 181, 22))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(70, 420, 461, 22))
        self.lineEditDBName = QLineEdit(Dialog)
        self.lineEditDBName.setObjectName(u"lineEditDBName")
        self.lineEditDBName.setGeometry(QRect(250, 30, 241, 32))
        self.lineEditDBName.setStyleSheet(u"background-color: white")
        self.lineEditTableName = QLineEdit(Dialog)
        self.lineEditTableName.setObjectName(u"lineEditTableName")
        self.lineEditTableName.setGeometry(QRect(250, 70, 171, 32))
        self.lineEditTableName.setStyleSheet(u"background-color: white")
        self.lineEditEmailAddress = QLineEdit(Dialog)
        self.lineEditEmailAddress.setObjectName(u"lineEditEmailAddress")
        self.lineEditEmailAddress.setGeometry(QRect(250, 140, 241, 32))
        self.lineEditEmailAddress.setStyleSheet(u"background-color: white")
        self.lineEditOldPassword = QLineEdit(Dialog)
        self.lineEditOldPassword.setObjectName(u"lineEditOldPassword")
        self.lineEditOldPassword.setGeometry(QRect(250, 190, 151, 32))
        self.lineEditOldPassword.setStyleSheet(u"background-color: white")
        self.lineEditOldPassword.setEchoMode(QLineEdit.Password)
        self.lineEditNewPassword = QLineEdit(Dialog)
        self.lineEditNewPassword.setObjectName(u"lineEditNewPassword")
        self.lineEditNewPassword.setGeometry(QRect(250, 250, 151, 32))
        self.lineEditNewPassword.setStyleSheet(u"background-color: white")
        self.lineEditNewPassword.setEchoMode(QLineEdit.Password)
        self.lineEditRePassword = QLineEdit(Dialog)
        self.lineEditRePassword.setObjectName(u"lineEditRePassword")
        self.lineEditRePassword.setGeometry(QRect(250, 300, 151, 32))
        self.lineEditRePassword.setStyleSheet(u"background-color: white")
        self.lineEditRePassword.setEchoMode(QLineEdit.Password)
        self.pushButtonChangePassword = QPushButton(Dialog)
        self.pushButtonChangePassword.setObjectName(u"pushButtonChangePassword")
        self.pushButtonChangePassword.setGeometry(QRect(210, 360, 221, 30))
        self.labelName = QLabel(Dialog)
        self.labelName.setObjectName(u"label_2")
        self.labelName.setGeometry(QRect(120, 10, 381, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter Database name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter table name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Email Address</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Old Password</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">New Password</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Re-enter New Password</span></p></body></html>", None))
        self.labelResponse.setText("")
        self.pushButtonChangePassword.setText(QCoreApplication.translate("Dialog", u"Change Password", None))
        self.labelName.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">2020041091-3-2-chpark-embeddedsoftware-midTerm</span></p></body></html>", None))
    # retranslateUi

