# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(237, 209)
        Dialog.setWindowOpacity(0.970000000000000)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 60, 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 60, 16))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 40, 113, 21))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 100, 113, 21))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 160, 113, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u767b\u9646\u754c\u9762", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55!", None))
    # retranslateUi
