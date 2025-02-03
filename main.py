import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.currency import Currency
from utils.scientefic import Scientefic
from utils.simple import Simple


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 322)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 272, 52))
        self.label.setStyleSheet('font: 32pt "Emblema One";')
        self.label.setObjectName("label")
        self.trigonometric_calculator = QtWidgets.QPushButton(Dialog)
        self.trigonometric_calculator.setGeometry(QtCore.QRect(10, 180, 411, 44))
        self.trigonometric_calculator.setStyleSheet("\n" 'font: 22pt "Black Ops One";')
        self.trigonometric_calculator.setObjectName("trigonometric_calculator")
        self.simple_button = QtWidgets.QPushButton(Dialog)
        self.simple_button.setGeometry(QtCore.QRect(10, 80, 411, 44))
        self.simple_button.setStyleSheet("\n" 'font: 22pt "Black Ops One";')
        self.simple_button.setObjectName("simple_button")
        self.scientefic_button = QtWidgets.QPushButton(Dialog)
        self.scientefic_button.setGeometry(QtCore.QRect(10, 130, 411, 44))
        self.scientefic_button.setStyleSheet("\n" 'font: 22pt "Black Ops One";')
        self.scientefic_button.setObjectName("scientefic_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Calculator"))
        self.trigonometric_calculator.setText(
            _translate("Dialog", "Currency Calculator")
        )
        self.simple_button.setText(_translate("Dialog", "Simple Calculator"))
        self.scientefic_button.setText(_translate("Dialog", "Scientefic Calculator"))


class Home(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 322)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 272, 52))
        self.label.setStyleSheet('font: 32pt "Emblema One";')
        self.label.setObjectName("label")
        self.trigonometric_calculator = QtWidgets.QPushButton(Dialog)
        self.trigonometric_calculator.setGeometry(QtCore.QRect(10, 180, 411, 44))
        self.trigonometric_calculator.setStyleSheet("\n" 'font: 22pt "Black Ops One";')
        self.trigonometric_calculator.setObjectName("trigonometric_calculator")
        self.simple_button = QtWidgets.QPushButton(Dialog)
        self.simple_button.setGeometry(QtCore.QRect(10, 80, 411, 44))
        self.simple_button.setStyleSheet("\n" 'font: 22pt "Black Ops One";')
        self.simple_button.setObjectName("simple_button")
        self.scientefic_button = QtWidgets.QPushButton(Dialog)
        self.scientefic_button.setGeometry(QtCore.QRect(10, 130, 411, 44))
        self.scientefic_button.setStyleSheet("\n" 'font: 22pt "Black Ops One";')
        self.scientefic_button.setObjectName("scientefic_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Calculator"))
        self.trigonometric_calculator.setText(
            _translate("Dialog", "Currency Calculator")
        )
        self.simple_button.setText(_translate("Dialog", "Simple Calculator"))
        self.scientefic_button.setText(_translate("Dialog", "Scientefic Calculator"))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        # uic.loadUi('maind.ui', self)
        Dialog = QtWidgets.QDialog()

        self.setupUi(self)
        self.retranslateUi(self)

        self.simple_button.clicked.connect(self.load_simple)
        self.scientefic_button.clicked.connect(self.load_scientefic)
        self.trigonometric_calculator.clicked.connect(self.load_currency)

    def load_currency(self):
        widget.setFixedHeight(300)
        widget.setFixedWidth(558)
        widget.setCurrentIndex(widget.currentIndex() + 3)

    def load_scientefic(self):
        widget.setFixedHeight(300)
        widget.setFixedWidth(440)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def load_simple(self):
        widget.setFixedHeight(416)
        widget.setFixedWidth(217)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print(widget.currentIndex())


Window = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main = Home()
simple = Simple()
science = Scientefic()
curr = Currency()
widget.addWidget(main)
widget.addWidget(simple)
widget.addWidget(science)
widget.addWidget(curr)
widget.setFixedHeight(322)
widget.setFixedWidth(424)

widget.show()
sys.exit(Window.exec())
