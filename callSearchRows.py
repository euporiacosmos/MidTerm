import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoSearchRows_chpark import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
    def SearchRows(self):
        sql="SELECT Password FROM " + self.ui.lineEditTableName.text() + " WHERE EmailAddress = '" + self.ui.lineEditEmailAddress.text() + "'"
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            if row == None:
                self.ui.labelResponse.setText("Record Not Found")
                self.ui.lineEditPassword.clear()
            else:
                self.ui.labelResponse.setText("Record Found")
                self.ui.lineEditPassword.setText(row[0])
        except Error as e:
            self.ui.labelResponse.setText("Error: " + str(e))
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

