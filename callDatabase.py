import sqlite3, sys
from PySide2.QtWidgets import QDialog, QApplication
from sqlite3 import Error

from demoDatabase_chpark import * # uic로 auto-generate한 클래스 import

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateDB.clicked.connect(self.createDatabase)
        self.show()

    def createDatabase(self):
        try: # 예외 처리
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".sqlite") # 교안과 다르게 확장자를 지정. 본인 스타일
            self.ui.labelResponse.setText("Database is created")
        except Error as e: # sqlite3 데이터베이스  예외 발생
            self.ui.labelResponse.setText("Some error has occured") # 데이터베이스 예외 발생 시 출력
        finally:
            conn.close()

if __name__ == "__main__": # 메인 함수
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
