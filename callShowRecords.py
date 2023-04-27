import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoShowRecords_chpark import *

rowNum = 1

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonFirst.clicked.connect(self.showFirstRow)
        self.ui.pushButtonPrevious.clicked.connect(self.showPreviousRow)
        self.ui.pushButtonNext.clicked.connect(self.showNextRow)
        self.ui.pushButtonLast.clicked.connect(self.showLastRow)
    def showFirstRow(self):
        conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM " + self.ui.lineEditTableName.text())
            row = cur.fetchone()
            if row:
                self.ui.lineEditEmailAddress.setText(row[rowNum-1])
                self.ui.lineEditPassword.setText(row[rowNum])
        except Error as e:
            self.ui.labelResponse.setText("Error: " + str(e))
    def showPreviousRow(self):
        conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM " + self.ui.lineEditTableName.text())
            row = cur.fetchone()
            if row:
                self.ui.lineEditEmailAddress.setText(row[rowNum-3])
                self.ui.lineEditPassword.setText(row[rowNum-2])
        except Error as e:
            self.ui.labelResponse.setText("Error: " + str(e))
    def showNextRow(self):
        conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM " + self.ui.lineEditTableName.text())
            row = cur.fetchone()
            if row:
                self.ui.lineEditEmailAddress.setText(row[rowNum+1])
                self.ui.lineEditPassword.setText(row[rowNum+2])
        except Error as e:
            self.ui.labelResponse.setText("Error: " + str(e))
    def showLastRow(self):
        conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM " + self.ui.lineEditTableName.text())
            row = cur.fetchone()
            if row:
                self.ui.lineEditEmailAddress.setText(row[-2])
                self.ui.lineEditPassword.setText(row[-1])
        except Error as e:
            self.ui.labelResponse.setText("Error: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
