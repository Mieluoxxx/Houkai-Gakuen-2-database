from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox('是否被选中')
        cb.stateChanged.connect(self.showState)

        btn = QPushButton('获取状态')
        btn.clicked.connect(lambda: print(cb.isChecked()))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        mainLayout.addWidget(btn)
        self.setLayout(mainLayout)

    def showState(self, state):
        print(state)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
