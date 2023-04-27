import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoInsertRowsInTable_chpark import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonInsertRow.clicked.connect(self.insertRow)
        self.show()

    def insertRow(self):
        sql = "INSERT INTO " + self.ui.lineEditTableName.text() + " VALUES (" + self.ui.lineEditEmailAddress.text() + ", " + self.ui.lineEditPassword.text() + ")"
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
            with conn:
                cur = conn.cursor()
                cur.execute(sql)
            self.ui.labelResponse.setText("Row inserted successfully")
        except Error as e:
            self.ui.labelResponse.setText("Error: " + str(e))
        finally:
            cur.close()
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())