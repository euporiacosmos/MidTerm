import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoDatabase_chpark import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateDB.clicked.connect(self.createDatabase_chpark)

    def createDatabase_chpark(self):
        try: # 예외 처리
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".sqlite")
            self.ui.labelResponse.setText("Database created")
        except Error as e:
            self.ui.labelResponse.setText("Some Error Has Occurred")
        finally:
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
