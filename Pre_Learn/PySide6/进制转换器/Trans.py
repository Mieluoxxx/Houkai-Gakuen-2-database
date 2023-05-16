# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Trans.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(386, 275)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.twoInputcomboBox = QComboBox(Form)
        self.twoInputcomboBox.setObjectName(u"twoInputcomboBox")
        self.twoInputcomboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputcomboBox, 4, 1, 1, 1)

        self.twoInput = QLineEdit(Form)
        self.twoInput.setObjectName(u"twoInput")
        self.twoInput.setMinimumSize(QSize(0, 40))
        self.twoInput.setStyleSheet(u".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(160, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.twoInput, 4, 0, 1, 1)

        self.oneInput = QLineEdit(Form)
        self.oneInput.setObjectName(u"oneInput")
        self.oneInput.setMinimumSize(QSize(0, 40))
        self.oneInput.setStyleSheet(u".QLineEdit{\n"
"	border-radius: 10%;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color: rgb(160, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.oneInput, 3, 0, 1, 1)

        self.dataTypecomboBox = QComboBox(Form)
        self.dataTypecomboBox.setObjectName(u"dataTypecomboBox")

        self.gridLayout.addWidget(self.dataTypecomboBox, 2, 0, 1, 2)

        self.originDataLabel = QLabel(Form)
        self.originDataLabel.setObjectName(u"originDataLabel")
        self.originDataLabel.setMaximumSize(QSize(1000, 30))
        font = QFont()
        font.setPointSize(24)
        self.originDataLabel.setFont(font)
        self.originDataLabel.setStyleSheet(u"color: rgb(160, 160, 160)")

        self.gridLayout.addWidget(self.originDataLabel, 0, 0, 1, 1)

        self.oneInputcomboBox = QComboBox(Form)
        self.oneInputcomboBox.setObjectName(u"oneInputcomboBox")
        self.oneInputcomboBox.setMinimumSize(QSize(195, 40))
        self.oneInputcomboBox.setStyleSheet(u"")

        self.gridLayout.addWidget(self.oneInputcomboBox, 3, 1, 1, 1)

        self.transDataLabel = QLabel(Form)
        self.transDataLabel.setObjectName(u"transDataLabel")
        self.transDataLabel.setMaximumSize(QSize(1000, 30))
        self.transDataLabel.setFont(font)
        self.transDataLabel.setStyleSheet(u"")

        self.gridLayout.addWidget(self.transDataLabel, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Trans", None))
        self.originDataLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.transDataLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

