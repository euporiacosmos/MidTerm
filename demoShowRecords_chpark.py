# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoShowRecords_chpark.ui'
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
        self.label.setGeometry(QRect(70, 60, 161, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 130, 161, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 260, 111, 22))
        self.lineEditDBName = QLineEdit(Dialog)
        self.lineEditDBName.setObjectName(u"lineEditDBName")
        self.lineEditDBName.setGeometry(QRect(230, 60, 221, 32))
        self.lineEditDBName.setStyleSheet(u"background-color: white")
        self.lineEditTableName = QLineEdit(Dialog)
        self.lineEditTableName.setObjectName(u"lineEditTableName")
        self.lineEditTableName.setGeometry(QRect(230, 120, 221, 32))
        self.lineEditTableName.setStyleSheet(u"background-color: white")
        self.pushButtonFirst = QPushButton(Dialog)
        self.pushButtonFirst.setObjectName(u"pushButtonFirst")
        self.pushButtonFirst.setGeometry(QRect(50, 190, 99, 30))
        self.pushButtonPrevious = QPushButton(Dialog)
        self.pushButtonPrevious.setObjectName(u"pushButtonPrevious")
        self.pushButtonPrevious.setGeometry(QRect(170, 190, 99, 30))
        self.pushButtonNext = QPushButton(Dialog)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setGeometry(QRect(300, 190, 99, 30))
        self.pushButtonLast = QPushButton(Dialog)
        self.pushButtonLast.setObjectName(u"pushButtonLast")
        self.pushButtonLast.setGeometry(QRect(430, 190, 99, 30))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 310, 68, 22))
        self.lineEditEmailAddress = QLineEdit(Dialog)
        self.lineEditEmailAddress.setObjectName(u"lineEditEmailAddress")
        self.lineEditEmailAddress.setGeometry(QRect(270, 260, 201, 32))
        self.lineEditEmailAddress.setStyleSheet(u"background-color: white")
        self.lineEditPassword = QLineEdit(Dialog)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(270, 310, 161, 32))
        self.lineEditPassword.setStyleSheet(u"background-color: white")
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(80, 390, 431, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 10, 391, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter database name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter table name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Email Address</span></p></body></html>", None))
        self.pushButtonFirst.setText(QCoreApplication.translate("Dialog", u"First Row", None))
        self.pushButtonPrevious.setText(QCoreApplication.translate("Dialog", u"Previous", None))
        self.pushButtonNext.setText(QCoreApplication.translate("Dialog", u"Next", None))
        self.pushButtonLast.setText(QCoreApplication.translate("Dialog", u"Last Row", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Password</span></p></body></html>", None))
        self.labelResponse.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">2020041091-3-2-chpark-embeddedsoftware-midterm</span></p></body></html>", None))
    # retranslateUi

