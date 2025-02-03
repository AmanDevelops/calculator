import math

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Scientefic(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 351, 51))
        self.label.setStyleSheet('font: 75 22pt "Arial";')
        self.label.setText("")
        self.label.setObjectName("label")
        self.dot = QtWidgets.QPushButton(Dialog)
        self.dot.setGeometry(QtCore.QRect(360, 240, 71, 51))
        self.dot.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.dot.setObjectName("dot")
        self.nine = QtWidgets.QPushButton(Dialog)
        self.nine.setGeometry(QtCore.QRect(360, 90, 71, 51))
        self.nine.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.nine.setObjectName("nine")
        self.zero = QtWidgets.QPushButton(Dialog)
        self.zero.setGeometry(QtCore.QRect(290, 240, 71, 51))
        self.zero.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.zero.setObjectName("zero")
        self.four = QtWidgets.QPushButton(Dialog)
        self.four.setGeometry(QtCore.QRect(220, 140, 71, 51))
        self.four.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.four.setObjectName("four")
        self.seven = QtWidgets.QPushButton(Dialog)
        self.seven.setGeometry(QtCore.QRect(220, 90, 71, 51))
        self.seven.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(Dialog)
        self.eight.setGeometry(QtCore.QRect(290, 90, 71, 51))
        self.eight.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.eight.setObjectName("eight")
        self.one = QtWidgets.QPushButton(Dialog)
        self.one.setGeometry(QtCore.QRect(220, 190, 71, 51))
        self.one.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.one.setObjectName("one")
        self.three = QtWidgets.QPushButton(Dialog)
        self.three.setGeometry(QtCore.QRect(360, 190, 71, 51))
        self.three.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.three.setObjectName("three")
        self.five = QtWidgets.QPushButton(Dialog)
        self.five.setGeometry(QtCore.QRect(290, 140, 71, 51))
        self.five.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.five.setObjectName("five")
        self.sign_change = QtWidgets.QPushButton(Dialog)
        self.sign_change.setGeometry(QtCore.QRect(220, 240, 71, 51))
        self.sign_change.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.sign_change.setObjectName("sign_change")
        self.six = QtWidgets.QPushButton(Dialog)
        self.six.setGeometry(QtCore.QRect(360, 140, 71, 51))
        self.six.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.six.setObjectName("six")
        self.two = QtWidgets.QPushButton(Dialog)
        self.two.setGeometry(QtCore.QRect(290, 190, 71, 51))
        self.two.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.two.setObjectName("two")
        self.cos = QtWidgets.QPushButton(Dialog)
        self.cos.setGeometry(QtCore.QRect(80, 90, 71, 51))
        self.cos.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.cos.setObjectName("cos")
        self.tan = QtWidgets.QPushButton(Dialog)
        self.tan.setGeometry(QtCore.QRect(150, 90, 71, 51))
        self.tan.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.tan.setObjectName("tan")
        self.cot = QtWidgets.QPushButton(Dialog)
        self.cot.setGeometry(QtCore.QRect(150, 140, 71, 51))
        self.cot.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.cot.setObjectName("cot")
        self.acos = QtWidgets.QPushButton(Dialog)
        self.acos.setGeometry(QtCore.QRect(80, 190, 71, 51))
        self.acos.setStyleSheet('font: 75 16pt "Georgia";\n' "")
        self.acos.setObjectName("acos")
        self.asin = QtWidgets.QPushButton(Dialog)
        self.asin.setGeometry(QtCore.QRect(10, 190, 71, 51))
        self.asin.setStyleSheet('font: 75 16pt "Georgia";\n' "")
        self.asin.setObjectName("asin")
        self.acot = QtWidgets.QPushButton(Dialog)
        self.acot.setGeometry(QtCore.QRect(150, 240, 71, 51))
        self.acot.setStyleSheet('font: 75 16pt "Georgia";\n' "")
        self.acot.setObjectName("acot")
        self.sin = QtWidgets.QPushButton(Dialog)
        self.sin.setGeometry(QtCore.QRect(10, 90, 71, 51))
        self.sin.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.sin.setObjectName("sin")
        self.asec = QtWidgets.QPushButton(Dialog)
        self.asec.setGeometry(QtCore.QRect(80, 240, 71, 51))
        self.asec.setStyleSheet('font: 75 16pt "Georgia";\n' "")
        self.asec.setObjectName("asec")
        self.acosec = QtWidgets.QPushButton(Dialog)
        self.acosec.setGeometry(QtCore.QRect(10, 240, 71, 51))
        self.acosec.setStyleSheet('font: 75 12pt "Georgia";\n' "\n" "")
        self.acosec.setObjectName("acosec")
        self.atan = QtWidgets.QPushButton(Dialog)
        self.atan.setGeometry(QtCore.QRect(150, 190, 71, 51))
        self.atan.setStyleSheet('font: 75 14pt "Georgia";\n' "")
        self.atan.setObjectName("atan")
        self.cosec = QtWidgets.QPushButton(Dialog)
        self.cosec.setGeometry(QtCore.QRect(10, 140, 71, 51))
        self.cosec.setStyleSheet('font: 75 16pt "Georgia";\n' "")
        self.cosec.setObjectName("cosec")
        self.sec = QtWidgets.QPushButton(Dialog)
        self.sec.setGeometry(QtCore.QRect(80, 140, 71, 51))
        self.sec.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.sec.setObjectName("sec")
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(360, 40, 71, 51))
        self.clear.setStyleSheet('font: 75 22pt "Georgia";\n' "")
        self.clear.setObjectName("clear")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 321, 16))
        self.label_2.setStyleSheet('font: 12pt "MS Shell Dlg 2";')
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dot.setText(_translate("Dialog", "."))
        self.nine.setText(_translate("Dialog", "9"))
        self.zero.setText(_translate("Dialog", "0"))
        self.four.setText(_translate("Dialog", "4"))
        self.seven.setText(_translate("Dialog", "7"))
        self.eight.setText(_translate("Dialog", "8"))
        self.one.setText(_translate("Dialog", "1"))
        self.three.setText(_translate("Dialog", "3"))
        self.five.setText(_translate("Dialog", "5"))
        self.sign_change.setText(_translate("Dialog", "-"))
        self.six.setText(_translate("Dialog", "6"))
        self.two.setText(_translate("Dialog", "2"))
        self.cos.setText(_translate("Dialog", "Cos"))
        self.tan.setText(_translate("Dialog", "Tan"))
        self.cot.setText(_translate("Dialog", "Cot"))
        self.acos.setText(_translate("Dialog", "Cos^-1"))
        self.asin.setText(_translate("Dialog", "Sin^-1"))
        self.acot.setText(_translate("Dialog", "Cot^-1"))
        self.sin.setText(_translate("Dialog", "Sin"))
        self.asec.setText(_translate("Dialog", "Sec^-1"))
        self.acosec.setText(_translate("Dialog", "Cosec^-1"))
        self.atan.setText(_translate("Dialog", "Tan^-1"))
        self.cosec.setText(_translate("Dialog", "Cosec"))
        self.sec.setText(_translate("Dialog", "Sec"))
        self.clear.setText(_translate("Dialog", "C"))
        self.label_2.setText(
            _translate("Dialog", "Arpit Kumar Verma, Azizul Hasan, Aman Pal")
        )

    def __init__(self):
        super().__init__()

        Dialog = QtWidgets.QDialog()

        self.setupUi(self)
        self.retranslateUi(self)

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
        self.clear.clicked.connect(self.pressedclear)
        self.dot.clicked.connect(self.presseddot)
        self.sign_change.clicked.connect(self.pressednegative)
        self.sin.clicked.connect(self.calcsin)
        self.cos.clicked.connect(self.calccos)
        self.tan.clicked.connect(self.calctan)
        self.cosec.clicked.connect(self.calccosec)
        self.sec.clicked.connect(self.calcsec)
        self.cot.clicked.connect(self.calccot)
        self.asin.clicked.connect(self.calcasin)
        self.acos.clicked.connect(self.calcacos)
        self.atan.clicked.connect(self.calcatan)
        self.acosec.clicked.connect(self.calcacosec)
        self.asec.clicked.connect(self.calcasec)
        self.acot.clicked.connect(self.calcacot)

    def calcsin(self):
        try:
            rad = float(self.label.text()) * (math.pi / 180)
            ans = str(math.sin(rad))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calccos(self):
        try:
            rad = float(self.label.text()) * (math.pi / 180)
            ans = str(math.cos(rad))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calctan(self):
        try:
            ans = str(math.tan(math.radians(float(self.label.text()))))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calccosec(self):
        try:
            rad = float(self.label.text()) * (math.pi / 180)
            ans = str(1 / math.sin(rad))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcsec(self):
        try:
            rad = float(self.label.text()) * (math.pi / 180)
            ans = str(1 / math.cos(rad))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calccot(self):
        try:
            rad = float(self.label.text()) * (math.pi / 180)
            ans = str(1 / math.tan(rad))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcasin(self):
        try:
            rad = float(self.label.text())
            ans = str(math.degrees(math.asin(rad)))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcacos(self):
        try:
            rad = float(self.label.text())
            ans = str(math.degrees(math.acos(rad)))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcatan(self):
        try:
            rad = float(self.label.text())
            ans = str(math.degrees(math.atan(rad)))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcacosec(self):
        try:
            rad = 1 / float(self.label.text())
            ans = str(math.degrees(math.asin(rad)))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcasec(self):
        try:
            rad = 1 / float(self.label.text())
            ans = str(math.degrees(math.acos(rad)))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def calcacot(self):
        try:
            rad = 1 / float(self.label.text())
            ans = str(math.degrees(math.atan(rad)))
            self.label.setText(ans)
        except:
            self.label.setText("Input has Invalid Domain")

    def pressedclear(self):
        self.label.setText("")

    def presseddot(self):
        text = self.label.text()
        if text != "":
            if text.find(".") == -1:
                self.label.setText(text + ".")

    def pressednegative(self):
        text = self.label.text()
        if text != "":
            if text[0] == "-":
                self.label.setText(text[1:])
            else:
                self.label.setText("-" + text)
        else:
            self.label.setText("-" + text)

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
