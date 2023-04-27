import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoCreateTable_chpark import *

tableDefinition = ""
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateTable.clicked.connect(self.createTable)
        self.ui.pushButtonAddColumn.clicked.connect(self.addColumns)
        self.show()

    def addColumns(self):
        global tableDefinition
        if tableDefinition == "":
            tableDefinition = "CREATE TABLA IF NOT EXISTS " + self.ui.lineEditTableName.text() + " (" + self.ui.lineEditColumnName.text() + " " + self.ui.comboBoxDataType.itemText(self.ui.comboBoxDataType.currentIndex()) + ")"
        else:
            tableDefinition += ", " + self.ui.lineEditColumnName.text() + " " + self.ui.comboBoxDataType.itemText(self.ui.comboBoxDataType.currentIndex())
        self.ui.lineEditColumnName.clear() # 교안과 다르게 한 부분
        self.ui.lineEditColumnName.setFocus()
    
    def createTable(self):
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text())
            cur = conn.cursor()
            cur.execute(tableDefinition)
            self.ui.labelResponse.setText("Table created successfully")
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