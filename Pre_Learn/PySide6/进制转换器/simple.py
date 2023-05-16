from PySide6.QtWidgets import QApplication, QWidget
from Trans import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 数据类型的字典
        self.lengthVar = {'米': 100, '千米': 100000, '分米': 10, '厘米': 1}
        self.weightVar = {'克': 1, '千克': 1000, '斤': 500}

        self.TypeDict = {'长度': self.lengthVar, '重量': self.weightVar}

        self.dataTypecomboBox.addItems(self.TypeDict.keys())
        self.oneInputcomboBox.addItems(self.lengthVar.keys())
        self.twoInputcomboBox.addItems(self.lengthVar.keys())
        self.bind()

    def bind(self):
        self.dataTypecomboBox.currentTextChanged.connect(self.typeChanged)
        self.pushButton.clicked.connect(self.calc)

    def calc(self):
        bigType = self.dataTypecomboBox.currentText()
        # 获取第一个输入框的值
        value = self.oneInput.text()
        if value == '':
            return

        currentType = self.oneInputcomboBox.currentText()
        transType = self.twoInputcomboBox.currentText()

        standardization = float(value) * self.TypeDict[bigType][currentType]
        result = standardization / self.TypeDict[bigType][transType]

        self.originDataLabel.setText(f'{value} {currentType} =')
        self.transDataLabel.setText(f'{result} {transType}')
        self.twoInput.setText(str(result))

    def typeChanged(self, text):
        self.oneInputcomboBox.clear()
        self.twoInputcomboBox.clear()

        self.oneInputcomboBox.addItems(self.TypeDict[text].keys())
        self.twoInputcomboBox.addItems(self.TypeDict[text].keys())


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
