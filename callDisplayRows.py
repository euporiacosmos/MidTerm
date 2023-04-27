import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoDisplayRowsOfTable_chpark import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDisplayRows.clicked.connect(self.displayRows)
        self.show()
    def displayRows(self):
        sql = "SELECT * FROM " + self.ui.lineEditTableName.text()
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".sqlite")
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            rowNum = 0
            for tuple in rows:
                self.ui.labelResponse.clear()
                colNum = 0
                for columns in tuple:
                    oneColumn = QTableWidgetItem(columns)
                    self.ui.tableWidget.setItem(rowNum, colNum, oneColumn)
                    colNum += 1
                rowNum += 1
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