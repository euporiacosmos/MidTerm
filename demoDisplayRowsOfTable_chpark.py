# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoDisplayRowsOfTable_chpark.ui'
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
        self.label.setGeometry(QRect(40, 22, 171, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 161, 22))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(50, 410, 471, 22))
        self.lineEditDBName = QLineEdit(Dialog)
        self.lineEditDBName.setObjectName(u"lineEditDBName")
        self.lineEditDBName.setGeometry(QRect(240, 20, 271, 32))
        self.lineEditDBName.setStyleSheet(u"background-color: white")
        self.lineEditTableName = QLineEdit(Dialog)
        self.lineEditTableName.setObjectName(u"lineEditTableName")
        self.lineEditTableName.setGeometry(QRect(240, 70, 271, 32))
        self.lineEditTableName.setStyleSheet(u"background-color: white")
        self.pushButtonDisplayRows = QPushButton(Dialog)
        self.pushButtonDisplayRows.setObjectName(u"pushButtonDisplayRows")
        self.pushButtonDisplayRows.setGeometry(QRect(220, 130, 151, 30))
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 180, 531, 192))
        self.tableWidget.setStyleSheet(u"background-color: white")
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 0, 401, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter database name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter table name</span></p></body></html>", None))
        self.labelResponse.setText("")
        self.pushButtonDisplayRows.setText(QCoreApplication.translate("Dialog", u"Display Rows", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">2020041091-3-2-chpark-embeddedsoftware-midTerm</span></p></body></html>", None))
    # retranslateUi

