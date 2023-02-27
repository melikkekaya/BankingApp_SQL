# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/BankingApp_SQL/customer_transfer_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customer_transfer_window(object):
    def setupUi(self, customer_transfer_window):
        customer_transfer_window.setObjectName("customer_transfer_window")
        customer_transfer_window.setWindowModality(QtCore.Qt.ApplicationModal)
        customer_transfer_window.resize(600, 700)
        customer_transfer_window.setMinimumSize(QtCore.QSize(600, 700))
        customer_transfer_window.setMaximumSize(QtCore.QSize(600, 700))
        customer_transfer_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        customer_transfer_window.setAcceptDrops(False)
        customer_transfer_window.setStyleSheet("background-color: rgb(241, 242, 248);")
        customer_transfer_window.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(customer_transfer_window)
        self.centralwidget.setObjectName("centralwidget")
        self.cstrfwdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.cstrfwdw_lbl_heading.setGeometry(QtCore.QRect(50, 30, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_heading.setFont(font)
        self.cstrfwdw_lbl_heading.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_heading.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.cstrfwdw_lbl_heading.setObjectName("cstrfwdw_lbl_heading")
        self.cstrfwdw_btn_returnmain = QtWidgets.QPushButton(self.centralwidget)
        self.cstrfwdw_btn_returnmain.setGeometry(QtCore.QRect(110, 580, 180, 70))
        self.cstrfwdw_btn_returnmain.setMinimumSize(QtCore.QSize(180, 70))
        self.cstrfwdw_btn_returnmain.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_btn_returnmain.setFont(font)
        self.cstrfwdw_btn_returnmain.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(187, 207, 237);\n"
"border:2px solid rgb(123, 169, 191);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cstrfwdw_btn_returnmain.setIcon(icon)
        self.cstrfwdw_btn_returnmain.setIconSize(QtCore.QSize(40, 40))
        self.cstrfwdw_btn_returnmain.setObjectName("cstrfwdw_btn_returnmain")
        self.cstrfwdw_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.cstrfwdw_btn_exit.setGeometry(QtCore.QRect(310, 580, 180, 70))
        self.cstrfwdw_btn_exit.setMinimumSize(QtCore.QSize(180, 70))
        self.cstrfwdw_btn_exit.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_btn_exit.setFont(font)
        self.cstrfwdw_btn_exit.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(187, 207, 237);\n"
"border:2px solid rgb(123, 169, 191);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cstrfwdw_btn_exit.setIcon(icon1)
        self.cstrfwdw_btn_exit.setIconSize(QtCore.QSize(40, 40))
        self.cstrfwdw_btn_exit.setObjectName("cstrfwdw_btn_exit")
        self.cstrfwdw_btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.cstrfwdw_btn_send.setGeometry(QtCore.QRect(200, 460, 180, 50))
        self.cstrfwdw_btn_send.setMinimumSize(QtCore.QSize(180, 50))
        self.cstrfwdw_btn_send.setMaximumSize(QtCore.QSize(180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_btn_send.setFont(font)
        self.cstrfwdw_btn_send.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(211, 224, 243);\n"
"border:2px solid rgb(123, 169, 191);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/fund.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cstrfwdw_btn_send.setIcon(icon2)
        self.cstrfwdw_btn_send.setIconSize(QtCore.QSize(35, 35))
        self.cstrfwdw_btn_send.setObjectName("cstrfwdw_btn_send")
        self.cstrfwdw_btn_moneyup = QtWidgets.QPushButton(self.centralwidget)
        self.cstrfwdw_btn_moneyup.setGeometry(QtCore.QRect(400, 390, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_btn_moneyup.setFont(font)
        self.cstrfwdw_btn_moneyup.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(123, 169, 191);\n"
"border:2px solid rgb(60, 121, 138);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}")
        self.cstrfwdw_btn_moneyup.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cstrfwdw_btn_moneyup.setIcon(icon3)
        self.cstrfwdw_btn_moneyup.setIconSize(QtCore.QSize(25, 25))
        self.cstrfwdw_btn_moneyup.setObjectName("cstrfwdw_btn_moneyup")
        self.cstrfwdw_btn_moneydown = QtWidgets.QPushButton(self.centralwidget)
        self.cstrfwdw_btn_moneydown.setGeometry(QtCore.QRect(130, 390, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_btn_moneydown.setFont(font)
        self.cstrfwdw_btn_moneydown.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(123, 169, 191);\n"
"border:2px solid rgb(60, 121, 138);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}\n"
"   ")
        self.cstrfwdw_btn_moneydown.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cstrfwdw_btn_moneydown.setIcon(icon4)
        self.cstrfwdw_btn_moneydown.setIconSize(QtCore.QSize(25, 25))
        self.cstrfwdw_btn_moneydown.setObjectName("cstrfwdw_btn_moneydown")
        self.cstrfwdw_spinbox_money = QtWidgets.QSpinBox(self.centralwidget)
        self.cstrfwdw_spinbox_money.setGeometry(QtCore.QRect(210, 390, 160, 40))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cstrfwdw_spinbox_money.setFont(font)
        self.cstrfwdw_spinbox_money.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.cstrfwdw_spinbox_money.setStyleSheet("font: 24pt \".AppleSystemUIFont\";\n"
"background-color: rgb(236, 236, 236);")
        self.cstrfwdw_spinbox_money.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cstrfwdw_spinbox_money.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cstrfwdw_spinbox_money.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.cstrfwdw_spinbox_money.setSuffix("")
        self.cstrfwdw_spinbox_money.setMinimum(0)
        self.cstrfwdw_spinbox_money.setMaximum(1000000)
        self.cstrfwdw_spinbox_money.setSingleStep(100)
        self.cstrfwdw_spinbox_money.setProperty("value", 0)
        self.cstrfwdw_spinbox_money.setObjectName("cstrfwdw_spinbox_money")
        self.cstrfwdw_lbl_resultmessage = QtWidgets.QLabel(self.centralwidget)
        self.cstrfwdw_lbl_resultmessage.setGeometry(QtCore.QRect(50, 512, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_resultmessage.setFont(font)
        self.cstrfwdw_lbl_resultmessage.setStyleSheet("")
        self.cstrfwdw_lbl_resultmessage.setText("")
        self.cstrfwdw_lbl_resultmessage.setAlignment(QtCore.Qt.AlignCenter)
        self.cstrfwdw_lbl_resultmessage.setObjectName("cstrfwdw_lbl_resultmessage")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 90, 491, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.punc = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.punc.setFont(font)
        self.punc.setStyleSheet("color: rgb(15, 42, 57);")
        self.punc.setObjectName("punc")
        self.gridLayout.addWidget(self.punc, 1, 1, 1, 1)
        self.punc_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.punc_3.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.punc_3.setFont(font)
        self.punc_3.setStyleSheet("color: rgb(15, 42, 57);")
        self.punc_3.setObjectName("punc_3")
        self.gridLayout.addWidget(self.punc_3, 0, 1, 1, 1)
        self.cstrfwdw_lbl_CSname_show = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_CSname_show.setFont(font)
        self.cstrfwdw_lbl_CSname_show.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_CSname_show.setText("")
        self.cstrfwdw_lbl_CSname_show.setObjectName("cstrfwdw_lbl_CSname_show")
        self.gridLayout.addWidget(self.cstrfwdw_lbl_CSname_show, 0, 2, 1, 1)
        self.cstrfwdw_lbl_CSname_heading = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_CSname_heading.setFont(font)
        self.cstrfwdw_lbl_CSname_heading.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_CSname_heading.setObjectName("cstrfwdw_lbl_CSname_heading")
        self.gridLayout.addWidget(self.cstrfwdw_lbl_CSname_heading, 0, 0, 1, 1)
        self.cstrfwdw_lbl_balanceheading = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_balanceheading.setFont(font)
        self.cstrfwdw_lbl_balanceheading.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_balanceheading.setObjectName("cstrfwdw_lbl_balanceheading")
        self.gridLayout.addWidget(self.cstrfwdw_lbl_balanceheading, 2, 0, 1, 1)
        self.punc_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.punc_2.setFont(font)
        self.punc_2.setStyleSheet("color: rgb(15, 42, 57);")
        self.punc_2.setObjectName("punc_2")
        self.gridLayout.addWidget(self.punc_2, 2, 1, 1, 1)
        self.cstrfwdw_lbl_CSID_heading = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_CSID_heading.setFont(font)
        self.cstrfwdw_lbl_CSID_heading.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_CSID_heading.setObjectName("cstrfwdw_lbl_CSID_heading")
        self.gridLayout.addWidget(self.cstrfwdw_lbl_CSID_heading, 1, 0, 1, 1)
        self.cstrfwdw_lbl_balanceshow = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_balanceshow.setFont(font)
        self.cstrfwdw_lbl_balanceshow.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_balanceshow.setText("")
        self.cstrfwdw_lbl_balanceshow.setObjectName("cstrfwdw_lbl_balanceshow")
        self.gridLayout.addWidget(self.cstrfwdw_lbl_balanceshow, 2, 2, 1, 1)
        self.cstrfwdw_lbl_CSID_show = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_CSID_show.setFont(font)
        self.cstrfwdw_lbl_CSID_show.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_CSID_show.setText("")
        self.cstrfwdw_lbl_CSID_show.setObjectName("cstrfwdw_lbl_CSID_show")
        self.gridLayout.addWidget(self.cstrfwdw_lbl_CSID_show, 1, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 270, 491, 43))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cstrfwdw_linedit_receivernumber = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.cstrfwdw_linedit_receivernumber.setMinimumSize(QtCore.QSize(241, 41))
        self.cstrfwdw_linedit_receivernumber.setMaximumSize(QtCore.QSize(265, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cstrfwdw_linedit_receivernumber.setFont(font)
        self.cstrfwdw_linedit_receivernumber.setStyleSheet("font: 24pt \".AppleSystemUIFont\";\n"
"background-color: rgb(225, 229, 241);")
        self.cstrfwdw_linedit_receivernumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.cstrfwdw_linedit_receivernumber.setMaxLength(10)
        self.cstrfwdw_linedit_receivernumber.setObjectName("cstrfwdw_linedit_receivernumber")
        self.gridLayout_2.addWidget(self.cstrfwdw_linedit_receivernumber, 0, 2, 1, 1)
        self.cstrfwdw_lbl_receiverheading = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cstrfwdw_lbl_receiverheading.setFont(font)
        self.cstrfwdw_lbl_receiverheading.setStyleSheet("color: rgb(15, 42, 57);")
        self.cstrfwdw_lbl_receiverheading.setObjectName("cstrfwdw_lbl_receiverheading")
        self.gridLayout_2.addWidget(self.cstrfwdw_lbl_receiverheading, 0, 1, 1, 1)
        self.cstrfwdw_radiobtn_inttrf = QtWidgets.QRadioButton(self.centralwidget)
        self.cstrfwdw_radiobtn_inttrf.setGeometry(QtCore.QRect(64, 330, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.cstrfwdw_radiobtn_inttrf.setFont(font)
        self.cstrfwdw_radiobtn_inttrf.setObjectName("cstrfwdw_radiobtn_inttrf")
        self.cstrfwdw_radiobtn_exttrf = QtWidgets.QRadioButton(self.centralwidget)
        self.cstrfwdw_radiobtn_exttrf.setGeometry(QtCore.QRect(310, 330, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.cstrfwdw_radiobtn_exttrf.setFont(font)
        self.cstrfwdw_radiobtn_exttrf.setObjectName("cstrfwdw_radiobtn_exttrf")
        customer_transfer_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(customer_transfer_window)
        self.statusbar.setObjectName("statusbar")
        customer_transfer_window.setStatusBar(self.statusbar)

        self.retranslateUi(customer_transfer_window)
        self.cstrfwdw_btn_moneyup.clicked['bool'].connect(self.cstrfwdw_spinbox_money.stepUp) # type: ignore
        self.cstrfwdw_btn_moneydown.clicked['bool'].connect(self.cstrfwdw_spinbox_money.stepDown) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(customer_transfer_window)

    def retranslateUi(self, customer_transfer_window):
        _translate = QtCore.QCoreApplication.translate
        customer_transfer_window.setWindowTitle(_translate("customer_transfer_window", "Money Transfer Window"))
        self.cstrfwdw_lbl_heading.setText(_translate("customer_transfer_window", "Money Transfer"))
        self.cstrfwdw_btn_returnmain.setText(_translate("customer_transfer_window", "  Back"))
        self.cstrfwdw_btn_exit.setText(_translate("customer_transfer_window", "  Exit"))
        self.cstrfwdw_btn_send.setText(_translate("customer_transfer_window", "SEND MONEY"))
        self.punc.setText(_translate("customer_transfer_window", ":"))
        self.punc_3.setText(_translate("customer_transfer_window", ":"))
        self.cstrfwdw_lbl_CSname_heading.setText(_translate("customer_transfer_window", "Customer Name"))
        self.cstrfwdw_lbl_balanceheading.setText(_translate("customer_transfer_window", "Your current balance"))
        self.punc_2.setText(_translate("customer_transfer_window", ":"))
        self.cstrfwdw_lbl_CSID_heading.setText(_translate("customer_transfer_window", "Customer ID"))
        self.cstrfwdw_lbl_receiverheading.setText(_translate("customer_transfer_window", "Recipient Number"))
        self.cstrfwdw_radiobtn_inttrf.setText(_translate("customer_transfer_window", "Internal Money Transfer"))
        self.cstrfwdw_radiobtn_exttrf.setText(_translate("customer_transfer_window", "External Money Transfer"))
