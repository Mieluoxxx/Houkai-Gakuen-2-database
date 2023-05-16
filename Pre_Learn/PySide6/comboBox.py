from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(['张三', '李四', '王五'])

        cb.currentTextChanged.connect(self.showName)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        self.setLayout(mainLayout)

    def showName(self, name):
        print(name)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
