# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoCreateTable_chpark.ui'
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
        self.label.setGeometry(QRect(40, 60, 161, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 130, 131, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 190, 111, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(257, 190, 81, 22))
        self.labelResponse = QLabel(Dialog)
        self.labelResponse.setObjectName(u"labelResponse")
        self.labelResponse.setGeometry(QRect(130, 400, 321, 22))
        self.lineEditDBName = QLineEdit(Dialog)
        self.lineEditDBName.setObjectName(u"lineEditDBName")
        self.lineEditDBName.setGeometry(QRect(220, 50, 251, 32))
        self.lineEditDBName.setStyleSheet(u"background-color: white")
        self.lineEditTableName = QLineEdit(Dialog)
        self.lineEditTableName.setObjectName(u"lineEditTableName")
        self.lineEditTableName.setGeometry(QRect(220, 120, 251, 32))
        self.lineEditTableName.setStyleSheet(u"background-color: white")
        self.lineEditColumnName = QLineEdit(Dialog)
        self.lineEditColumnName.setObjectName(u"lineEditColumnName")
        self.lineEditColumnName.setGeometry(QRect(20, 230, 171, 32))
        self.lineEditColumnName.setStyleSheet(u"background-color: white")
        self.pushButtonAddColumn = QPushButton(Dialog)
        self.pushButtonAddColumn.setObjectName(u"pushButtonAddColumn")
        self.pushButtonAddColumn.setGeometry(QRect(450, 230, 121, 30))
        self.comboBoxDataType = QComboBox(Dialog)
        self.comboBoxDataType.addItem("")
        self.comboBoxDataType.addItem("")
        self.comboBoxDataType.setObjectName(u"comboBoxDataType")
        self.comboBoxDataType.setGeometry(QRect(220, 230, 181, 32))
        self.comboBoxDataType.setEditable(False)
        self.pushButtonCreateTable = QPushButton(Dialog)
        self.pushButtonCreateTable.setObjectName(u"pushButtonCreateTable")
        self.pushButtonCreateTable.setGeometry(QRect(240, 320, 141, 30))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 10, 391, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter database name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Enter table name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Column Name</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600; color:#00008b;\">Data Type</span></p></body></html>", None))
        self.labelResponse.setText("")
        self.pushButtonAddColumn.setText(QCoreApplication.translate("Dialog", u"Add Column", None))
        self.comboBoxDataType.setItemText(0, QCoreApplication.translate("Dialog", u"integer", None))
        self.comboBoxDataType.setItemText(1, QCoreApplication.translate("Dialog", u"text", None))

        self.pushButtonCreateTable.setText(QCoreApplication.translate("Dialog", u"Create Table", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">2020041091-3-2-chpark-embeddedsoftware-midTerm</span></p></body></html>", None))
    # retranslateUi

