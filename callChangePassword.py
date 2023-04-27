import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error
from hashlib import sha256 # 교안과 다르게 한 부분

from demoChangePassword_chpark import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonChangePassword.clicked.connect(self.changePassword)
        self.show()
    def changePassword(self):
        READ = "SELECT * FROM " + self.ui.lineEditTableName.text() + " WHERE EmailAddress = " + self.ui.lineEditEmailAddress.text() + " AND Password = " + sha256(self.ui.lineEditOldPassword.text())
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
            cur = conn.cursor()
            cur.execute(READ)
            row = cur.fetchone()
            if row == None:
                self.ui.labelResponse.setText("Record Not Found")
                self.ui.lineEditPassword.clear()
            else:
                if self.ui.lineEditNewPassword.text() == self.ui.lineEditConfirmPassword.text():
                    UPDATE = "UPDATE " + self.ui.lineEditTableName.text() + " SET Password = " + sha256(self.ui.lineEditNewPassword.text()) + " WHERE EmailAddress = " + self.ui.lineEditEmailAddress.text()
                    with conn:
                        cur.execute(UPDATE)
                        self.ui.labelResponse.setText("Password Changed") 
                else:
                    self.ui.labelResponse.setText("Passwords Don't Match")
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