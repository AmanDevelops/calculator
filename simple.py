from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

import sys


class Simple(QDialog):
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(217, 416)
                self.close_brac = QtWidgets.QPushButton(Dialog)
                self.close_brac.setGeometry(QtCore.QRect(60, 100, 51, 51))
                self.close_brac.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.close_brac.setObjectName("close_brac")
                self.three = QtWidgets.QPushButton(Dialog)
                self.three.setGeometry(QtCore.QRect(110, 300, 51, 51))
                self.three.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.three.setObjectName("three")
                self.sign_change = QtWidgets.QPushButton(Dialog)
                self.sign_change.setGeometry(QtCore.QRect(10, 350, 51, 51))
                self.sign_change.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.sign_change.setObjectName("sign_change")
                self.eight = QtWidgets.QPushButton(Dialog)
                self.eight.setGeometry(QtCore.QRect(60, 200, 51, 51))
                self.eight.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.eight.setObjectName("eight")
                self.clear_current = QtWidgets.QPushButton(Dialog)
                self.clear_current.setGeometry(QtCore.QRect(60, 150, 51, 51))
                self.clear_current.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.clear_current.setObjectName("clear_current")
                self.seven = QtWidgets.QPushButton(Dialog)
                self.seven.setGeometry(QtCore.QRect(10, 200, 51, 51))
                self.seven.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.seven.setObjectName("seven")
                self.zero = QtWidgets.QPushButton(Dialog)
                self.zero.setGeometry(QtCore.QRect(60, 350, 51, 51))
                self.zero.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.zero.setObjectName("zero")
                self.delete_2 = QtWidgets.QPushButton(Dialog)
                self.delete_2.setGeometry(QtCore.QRect(110, 150, 51, 51))
                self.delete_2.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.delete_2.setObjectName("delete_2")
                self.division = QtWidgets.QPushButton(Dialog)
                self.division.setGeometry(QtCore.QRect(160, 150, 51, 51))
                self.division.setStyleSheet("background-color: rgb(255, 140, 0);\n"
        "font: 22pt \"MS Shell Dlg 2\";")
                self.division.setObjectName("division")
                self.multiply = QtWidgets.QPushButton(Dialog)
                self.multiply.setGeometry(QtCore.QRect(160, 200, 51, 51))
                self.multiply.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.multiply.setObjectName("multiply")
                self.plus = QtWidgets.QPushButton(Dialog)
                self.plus.setGeometry(QtCore.QRect(160, 300, 51, 51))
                self.plus.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.plus.setObjectName("plus")
                self.subtract = QtWidgets.QPushButton(Dialog)
                self.subtract.setGeometry(QtCore.QRect(160, 250, 51, 51))
                self.subtract.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);\n"
        "")
                self.subtract.setObjectName("subtract")
                self.six = QtWidgets.QPushButton(Dialog)
                self.six.setGeometry(QtCore.QRect(110, 250, 51, 51))
                self.six.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.six.setObjectName("six")
                self.clear_all = QtWidgets.QPushButton(Dialog)
                self.clear_all.setGeometry(QtCore.QRect(10, 150, 51, 51))
                self.clear_all.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.clear_all.setObjectName("clear_all")
                self.equal = QtWidgets.QPushButton(Dialog)
                self.equal.setGeometry(QtCore.QRect(160, 350, 51, 51))
                self.equal.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.equal.setObjectName("equal")
                self.dot = QtWidgets.QPushButton(Dialog)
                self.dot.setGeometry(QtCore.QRect(110, 350, 51, 51))
                self.dot.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.dot.setObjectName("dot")
                self.nine = QtWidgets.QPushButton(Dialog)
                self.nine.setGeometry(QtCore.QRect(110, 200, 51, 51))
                self.nine.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.nine.setObjectName("nine")
                self.open_brac = QtWidgets.QPushButton(Dialog)
                self.open_brac.setGeometry(QtCore.QRect(10, 100, 51, 51))
                self.open_brac.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.open_brac.setObjectName("open_brac")
                self.four = QtWidgets.QPushButton(Dialog)
                self.four.setGeometry(QtCore.QRect(10, 250, 51, 51))
                self.four.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.four.setObjectName("four")
                self.five = QtWidgets.QPushButton(Dialog)
                self.five.setGeometry(QtCore.QRect(60, 250, 51, 51))
                self.five.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.five.setObjectName("five")
                self.one = QtWidgets.QPushButton(Dialog)
                self.one.setGeometry(QtCore.QRect(10, 300, 51, 51))
                self.one.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.one.setObjectName("one")
                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(10, 30, 201, 41))
                self.label.setStyleSheet("font: 22pt \"Georgia\";")
                self.label.setText("")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(6, 10, 211, 16))
                self.label_2.setObjectName("label_2")
                self.two = QtWidgets.QPushButton(Dialog)
                self.two.setGeometry(QtCore.QRect(60, 300, 51, 51))
                self.two.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "")
                self.two.setObjectName("two")
                self.square = QtWidgets.QPushButton(Dialog)
                self.square.setGeometry(QtCore.QRect(160, 100, 51, 51))
                self.square.setStyleSheet("background-color: rgb(255, 140, 0);\n"
        "font: 22pt \"MS Shell Dlg 2\";")
                self.square.setObjectName("square")
                self.root = QtWidgets.QPushButton(Dialog)
                self.root.setGeometry(QtCore.QRect(110, 100, 51, 51))
                self.root.setStyleSheet("font: 75 22pt \"Georgia\";\n"
        "background-color: rgb(255, 140, 0);")
                self.root.setObjectName("root")

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
                self.close_brac.setText(_translate("Dialog", ")"))
                self.three.setText(_translate("Dialog", "3"))
                self.sign_change.setText(_translate("Dialog", "-"))
                self.eight.setText(_translate("Dialog", "8"))
                self.clear_current.setText(_translate("Dialog", "C"))
                self.seven.setText(_translate("Dialog", "7"))
                self.zero.setText(_translate("Dialog", "0"))
                self.delete_2.setText(_translate("Dialog", "Del"))
                self.division.setText(_translate("Dialog", "÷"))
                self.multiply.setText(_translate("Dialog", "×"))
                self.plus.setText(_translate("Dialog", "+"))
                self.subtract.setText(_translate("Dialog", "-"))
                self.six.setText(_translate("Dialog", "6"))
                self.clear_all.setText(_translate("Dialog", "CA"))
                self.equal.setText(_translate("Dialog", "="))
                self.dot.setText(_translate("Dialog", "."))
                self.nine.setText(_translate("Dialog", "9"))
                self.open_brac.setText(_translate("Dialog", "("))
                self.four.setText(_translate("Dialog", "4"))
                self.five.setText(_translate("Dialog", "5"))
                self.one.setText(_translate("Dialog", "1"))
                self.label_2.setText(_translate("Dialog", "Arpit Kumar Verma, Azizul Hasan, Aman Pal"))
                self.two.setText(_translate("Dialog", "2"))
                self.square.setText(_translate("Dialog", "Sqr"))
                self.root.setText(_translate("Dialog", "√"))

        def __init__(self):
                super().__init__()

                #uic.loadUi("simpled.ui", self)
                self.setWindowTitle("Simple Calculator")

                Dialog = QtWidgets.QDialog()

                self.setupUi(self)
                self.retranslateUi(self)
                
                self.open_brac.clicked.connect(self.pressed_brac_open)
                self.close_brac.clicked.connect(self.pressed_brac_close)
                self.root.clicked.connect(self.pressed_root)
                self.square.clicked.connect(self.pressed_square)
                self.subtract.clicked.connect(self.pressed_minus)
                self.equal.clicked.connect(self.pressed_equal)
                self.zero.clicked.connect(self.pressed0)
                self.one.clicked.connect(self.pressed1)
                self.two.clicked.connect(self.pressed2)
                self.three.clicked.connect(self.pressed3)
                self.four.clicked.connect(self.pressed4)
                self.five.clicked.connect(self.pressed5)
                self.six.clicked.connect(self.pressed6)
                self.seven.clicked.connect(self.pressed7)
                self.eight.clicked.connect(self.pressed8)
                self.nine.clicked.connect(self.pressed9)
                self.division.clicked.connect(self.pressed_div)
                self.multiply.clicked.connect(self.pressed_mul)
                self.plus.clicked.connect(self.pressed_plus)
                self.dot.clicked.connect(self.pressed_point)
                self.clear_current.clicked.connect(self.pressed_clear)
                self.delete_2.clicked.connect(self.pressed_back_space)
                self.show()

        def pressed_equal(self):

                
                equation = self.label.text()

                try:
                        
                        
                        final_equation = compile(equation, "<string>", "eval")
                        ans = eval(final_equation)

                        
                        self.label.setText(str(ans))

                except:
                        
                        self.label.setText("Wrong Input")

        def pressed_back_space(self):
                text = self.label.text()
                length = len(text)
                self.label.setText(text[0:length-1])

        def pressed_brac_open(self):
                text = self.label.text()
                self.label.setText(text+ '(')
        def pressed_brac_close(self):
                text = self.label.text()
                self.label.setText(text+ ')')
        def pressed_root(self):
                text = self.label.text()
                self.label.setText(text+ '**0.5')
                
        def pressed_square(self):
                text = self.label.text()
                self.label.setText(text+ '**2')

        def pressed_plus(self):
                
                text = self.label.text()
                self.label.setText(text + "+")

        def pressed_minus(self):
                
                text = self.label.text()
                self.label.setText(text + "-")

        def pressed_div(self):
                
                text = self.label.text()
                self.label.setText(text + "/")

        def pressed_mul(self):
                
                text = self.label.text()
                self.label.setText(text + "*")

        def pressed_point(self):
                
                text = self.label.text()
                if text != '':
                        if text.find('.') == -1:
                                self.label.setText(text+'.')

        def pressed0(self):
                
                text = self.label.text()
                self.label.setText(text + "0")

        def pressed1(self):
                
                text = self.label.text()
                self.label.setText(text + "1")

        def pressed2(self):
                
                text = self.label.text()
                self.label.setText(text + "2")

        def pressed3(self):
                
                text = self.label.text()
                self.label.setText(text + "3")

        def pressed4(self):
                
                text = self.label.text()
                self.label.setText(text + "4")

        def pressed5(self):
                
                text = self.label.text()
                self.label.setText(text + "5")

        def pressed6(self):
                
                text = self.label.text()
                self.label.setText(text + "6")

        def pressed7(self):
                
                text = self.label.text()
                self.label.setText(text + "7")

        def pressed8(self):
                
                text = self.label.text()
                self.label.setText(text + "8")

        def pressed9(self):
                
                text = self.label.text()
                self.label.setText(text + "9")

        def pressed_clear(self):
                
                self.label.setText("")

        def pressed_del(self):
                
                text = self.label.text()
                print(text[:len(text)-1])
                self.label.setText(text[:len(text)-1])
        




