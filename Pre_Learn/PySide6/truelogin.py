from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from loginUI import Ui_Dialog


class MyWindow(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFuc)

    def loginFuc(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if account == '123' and password == '123':
            print('登录成功')
        else:
            print('登录失败')


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
