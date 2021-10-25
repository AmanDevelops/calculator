from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import requests
import json



class Currency(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 20, 111, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 271, 41))
        self.comboBox.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(310, 60, 211, 41))
        self.lineEdit.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 120, 121, 41))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 180, 251, 41))
        self.lineEdit_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 120, 271, 41))
        self.comboBox_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Arpit, Aman, Azizul"))
        self.pushButton.setText(_translate("Dialog", "Convert"))
    def __init__(self):
        super().__init__()

        #uic.loadUi("currency.ui", self)
        Dialog = QtWidgets.QDialog()

        self.setupUi(self)
        self.retranslateUi(self)

        currency_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT',
                         'BGN', 'BHD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BZD', 'CAD', 'CHF', 'CLP', 'CNY',
                         'COP', 'CRC', 'CZK', 'DKK', 'DOP', 'DZD', 'EGP', 'ETB', 'EUR', 'FJD', 'GBP', 'GEL', 'GHS',
                         'GMD', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JEP', 'JMD',
                         'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KRW', 'KWD', 'KYD', 'KZT', 'LBP', 'LKR', 'MAD', 'MDL',
                         'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MUR', 'MVR', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
                         'NOK', 'NPR', 'NZD', 'OMR', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD',
                         'RUB', 'RWF', 'SAR', 'SCR', 'SEK', 'SGD', 'STD', 'SYP', 'THB', 'TND', 'TRY', 'TTD', 'TWD',
                         'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF',
                         'ZAR', 'ZMW']
        currency_name = {
            "AED": "United Arab Emirates Dirham",
            "AFN": "Afghan Afghani",
            "ALL": "Albanian Lek",
            "AMD": "Armenian Dram",
            "ANG": "Netherlands Antillean Guilder",
            "AOA": "Angolan Kwanza",
            "ARS": "Argentine Peso",
            "AUD": "Australian Dollar",
            "AWG": "Aruban Florin",
            "AZN": "Azerbaijani Manat",
            "BAM": "Bosnia-Herzegovina Convertible Mark",
            "BBD": "Barbadian Dollar",
            "BDT": "Bangladeshi Taka",
            "BGN": "Bulgarian Lev",
            "BHD": "Bahraini Dinar",
            "BIF": "Burundian Franc",
            "BMD": "Bermudan Dollar",
            "BND": "Brunei Dollar",
            "BOB": "Bolivian Boliviano",
            "BRL": "Brazilian Real",
            "BSD": "Bahamian Dollar",
            "BTC": "Bitcoin",
            "BTN": "Bhutanese Ngultrum",
            "BWP": "Botswanan Pula",
            "BYN": "Belarusian Ruble",
            "BZD": "Belize Dollar",
            "CAD": "Canadian Dollar",
            "CDF": "Congolese Franc",
            "CHF": "Swiss Franc",
            "CLF": "Chilean Unit of Account (UF)",
            "CLP": "Chilean Peso",
            "CNH": "Chinese Yuan (Offshore)",
            "CNY": "Chinese Yuan",
            "COP": "Colombian Peso",
            "CRC": "Costa Rican Colón",
            "CUC": "Cuban Convertible Peso",
            "CUP": "Cuban Peso",
            "CVE": "Cape Verdean Escudo",
            "CZK": "Czech Republic Koruna",
            "DJF": "Djiboutian Franc",
            "DKK": "Danish Krone",
            "DOP": "Dominican Peso",
            "DZD": "Algerian Dinar",
            "EGP": "Egyptian Pound",
            "ERN": "Eritrean Nakfa",
            "ETB": "Ethiopian Birr",
            "EUR": "Euro",
            "FJD": "Fijian Dollar",
            "FKP": "Falkland Islands Pound",
            "GBP": "British Pound Sterling",
            "GEL": "Georgian Lari",
            "GGP": "Guernsey Pound",
            "GHS": "Ghanaian Cedi",
            "GIP": "Gibraltar Pound",
            "GMD": "Gambian Dalasi",
            "GNF": "Guinean Franc",
            "GTQ": "Guatemalan Quetzal",
            "GYD": "Guyanaese Dollar",
            "HKD": "Hong Kong Dollar",
            "HNL": "Honduran Lempira",
            "HRK": "Croatian Kuna",
            "HTG": "Haitian Gourde",
            "HUF": "Hungarian Forint",
            "IDR": "Indonesian Rupiah",
            "ILS": "Israeli New Sheqel",
            "IMP": "Manx pound",
            "INR": "Indian Rupee",
            "IQD": "Iraqi Dinar",
            "IRR": "Iranian Rial",
            "ISK": "Icelandic Króna",
            "JEP": "Jersey Pound",
            "JMD": "Jamaican Dollar",
            "JOD": "Jordanian Dinar",
            "JPY": "Japanese Yen",
            "KES": "Kenyan Shilling",
            "KGS": "Kyrgystani Som",
            "KHR": "Cambodian Riel",
            "KMF": "Comorian Franc",
            "KPW": "North Korean Won",
            "KRW": "South Korean Won",
            "KWD": "Kuwaiti Dinar",
            "KYD": "Cayman Islands Dollar",
            "KZT": "Kazakhstani Tenge",
            "LAK": "Laotian Kip",
            "LBP": "Lebanese Pound",
            "LKR": "Sri Lankan Rupee",
            "LRD": "Liberian Dollar",
            "LSL": "Lesotho Loti",
            "LYD": "Libyan Dinar",
            "MAD": "Moroccan Dirham",
            "MDL": "Moldovan Leu",
            "MGA": "Malagasy Ariary",
            "MKD": "Macedonian Denar",
            "MMK": "Myanma Kyat",
            "MNT": "Mongolian Tugrik",
            "MOP": "Macanese Pataca",
            "MRO": "Mauritanian Ouguiya (pre-2018)",
            "MRU": "Mauritanian Ouguiya",
            "MUR": "Mauritian Rupee",
            "MVR": "Maldivian Rufiyaa",
            "MWK": "Malawian Kwacha",
            "MXN": "Mexican Peso",
            "MYR": "Malaysian Ringgit",
            "MZN": "Mozambican Metical",
            "NAD": "Namibian Dollar",
            "NGN": "Nigerian Naira",
            "NIO": "Nicaraguan Córdoba",
            "NOK": "Norwegian Krone",
            "NPR": "Nepalese Rupee",
            "NZD": "New Zealand Dollar",
            "OMR": "Omani Rial",
            "PAB": "Panamanian Balboa",
            "PEN": "Peruvian Nuevo Sol",
            "PGK": "Papua New Guinean Kina",
            "PHP": "Philippine Peso",
            "PKR": "Pakistani Rupee",
            "PLN": "Polish Zloty",
            "PYG": "Paraguayan Guarani",
            "QAR": "Qatari Rial",
            "RON": "Romanian Leu",
            "RSD": "Serbian Dinar",
            "RUB": "Russian Ruble",
            "RWF": "Rwandan Franc",
            "SAR": "Saudi Riyal",
            "SBD": "Solomon Islands Dollar",
            "SCR": "Seychellois Rupee",
            "SDG": "Sudanese Pound",
            "SEK": "Swedish Krona",
            "SGD": "Singapore Dollar",
            "SHP": "Saint Helena Pound",
            "SLL": "Sierra Leonean Leone",
            "SOS": "Somali Shilling",
            "SRD": "Surinamese Dollar",
            "SSP": "South Sudanese Pound",
            "STD": "São Tomé and Príncipe Dobra (pre-2018)",
            "STN": "São Tomé and Príncipe Dobra",
            "SVC": "Salvadoran Colón",
            "SYP": "Syrian Pound",
            "SZL": "Swazi Lilangeni",
            "THB": "Thai Baht",
            "TJS": "Tajikistani Somoni",
            "TMT": "Turkmenistani Manat",
            "TND": "Tunisian Dinar",
            "TOP": "Tongan Pa'anga",
            "TRY": "Turkish Lira",
            "TTD": "Trinidad and Tobago Dollar",
            "TWD": "New Taiwan Dollar",
            "TZS": "Tanzanian Shilling",
            "UAH": "Ukrainian Hryvnia",
            "UGX": "Ugandan Shilling",
            "USD": "United States Dollar",
            "UYU": "Uruguayan Peso",
            "UZS": "Uzbekistan Som",
            "VEF": "Venezuelan Bolívar Fuerte (Old)",
            "VES": "Venezuelan Bolívar Soberano",
            "VND": "Vietnamese Dong",
            "VUV": "Vanuatu Vatu",
            "WST": "Samoan Tala",
            "XAF": "CFA Franc BEAC",
            "XAG": "Silver Ounce",
            "XAU": "Gold Ounce",
            "XCD": "East Caribbean Dollar",
            "XDR": "Special Drawing Rights",
            "XOF": "CFA Franc BCEAO",
            "XPD": "Palladium Ounce",
            "XPF": "CFP Franc",
            "XPT": "Platinum Ounce",
            "YER": "Yemeni Rial",
            "ZAR": "South African Rand",
            "ZMW": "Zambian Kwacha",
            "ZWL": "Zimbabwean Dollar"
        }
        for x in currency_list:
            self.comboBox.addItem(currency_name[x])
            self.comboBox_2.addItem(currency_name[x])

        self.pushButton.clicked.connect(self.convert)

        self.show()
    def convert(self):
        currency_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT',
                         'BGN', 'BHD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BZD', 'CAD', 'CHF', 'CLP', 'CNY',
                         'COP', 'CRC', 'CZK', 'DKK', 'DOP', 'DZD', 'EGP', 'ETB', 'EUR', 'FJD', 'GBP', 'GEL', 'GHS',
                         'GMD', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JEP', 'JMD',
                         'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KRW', 'KWD', 'KYD', 'KZT', 'LBP', 'LKR', 'MAD', 'MDL',
                         'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MUR', 'MVR', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO',
                         'NOK', 'NPR', 'NZD', 'OMR', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD',
                         'RUB', 'RWF', 'SAR', 'SCR', 'SEK', 'SGD', 'STD', 'SYP', 'THB', 'TND', 'TRY', 'TTD', 'TWD',
                         'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF',
                         'ZAR', 'ZMW']
        from_cur = currency_list[self.comboBox.currentIndex()]

        to_cur = currency_list[self.comboBox_2.currentIndex()]

        amount = self.lineEdit.text()
        if amount != '':
            try:
                r = requests.get('https://api.exchangerate.host/latest?base='+from_cur+'&symbols='+to_cur+'&amount='+amount).text
                res = json.loads(r)
                self.lineEdit_2.setText(str(res['rates'][to_cur]))
            except:
                self.lineEdit_2.setText('Could Not Connect To Internet')
        else:
            self.lineEdit_2.setText('Please Enter Amount')