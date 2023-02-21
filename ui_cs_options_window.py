# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\90506\Documents\GitHub\BankingApp_SQL\cs_options_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cs_options_window(object):
    def setupUi(self, cs_options_window):
        cs_options_window.setObjectName("cs_options_window")
        cs_options_window.resize(600, 700)
        cs_options_window.setStyleSheet("background-color: rgb(5, 130, 202);")
        self.centralwidget = QtWidgets.QWidget(cs_options_window)
        self.centralwidget.setObjectName("centralwidget")
        self.csoptwdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.csoptwdw_lbl_heading.setGeometry(QtCore.QRect(110, 20, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.csoptwdw_lbl_heading.setFont(font)
        self.csoptwdw_lbl_heading.setObjectName("csoptwdw_lbl_heading")
        self.csoptwdw_lbl_showname = QtWidgets.QLabel(self.centralwidget)
        self.csoptwdw_lbl_showname.setGeometry(QtCore.QRect(300, 20, 171, 81))
        self.csoptwdw_lbl_showname.setText("")
        self.csoptwdw_lbl_showname.setObjectName("csoptwdw_lbl_showname")
        self.optwdw_btn_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.optwdw_btn_transfer.setGeometry(QtCore.QRect(160, 260, 260, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.optwdw_btn_transfer.setFont(font)
        self.optwdw_btn_transfer.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 100, 148);\n"
"\n"
"border:2px solid rgb(0, 150, 199);\n"
"border-radius:20px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(0, 150, 199);\n"
"}")
        self.optwdw_btn_transfer.setObjectName("optwdw_btn_transfer")
        self.optwdw_btn_banktr = QtWidgets.QPushButton(self.centralwidget)
        self.optwdw_btn_banktr.setGeometry(QtCore.QRect(160, 150, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.optwdw_btn_banktr.setFont(font)
        self.optwdw_btn_banktr.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 100, 148);\n"
"\n"
"border:2px solid rgb(0, 150, 199);\n"
"border-radius:20px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(0, 150, 199);\n"
"}")
        self.optwdw_btn_banktr.setObjectName("optwdw_btn_banktr")
        self.optwdw_btn_editinf = QtWidgets.QPushButton(self.centralwidget)
        self.optwdw_btn_editinf.setGeometry(QtCore.QRect(160, 370, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.optwdw_btn_editinf.setFont(font)
        self.optwdw_btn_editinf.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 100, 148);\n"
"\n"
"border:2px solid rgb(0, 150, 199);\n"
"border-radius:20px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(0, 150, 199);\n"
"}")
        self.optwdw_btn_editinf.setObjectName("optwdw_btn_editinf")
        self.optwdw_btn_bankstt = QtWidgets.QPushButton(self.centralwidget)
        self.optwdw_btn_bankstt.setGeometry(QtCore.QRect(160, 480, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.optwdw_btn_bankstt.setFont(font)
        self.optwdw_btn_bankstt.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 100, 148);\n"
"\n"
"border:2px solid rgb(0, 150, 199);\n"
"border-radius:20px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(0, 150, 199);\n"
"}")
        self.optwdw_btn_bankstt.setObjectName("optwdw_btn_bankstt")
        self.optwdw_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.optwdw_btn_back.setGeometry(QtCore.QRect(100, 590, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.optwdw_btn_back.setFont(font)
        self.optwdw_btn_back.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 150, 199);\n"
"   border-color: rgb(66, 167, 255);\n"
"   border-bottom-color: rgb(255, 255, 255);\n"
"   border:2px solid rgb(202, 240, 248);\n"
"   border-radius:20px;\n"
"   border-color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(202, 240, 248);\n"
"}\n"
"    \n"
"   ")
        self.optwdw_btn_back.setObjectName("optwdw_btn_back")
        self.optwdw_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.optwdw_btn_exit.setGeometry(QtCore.QRect(340, 590, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.optwdw_btn_exit.setFont(font)
        self.optwdw_btn_exit.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 150, 199);\n"
"   border-color: rgb(66, 167, 255);\n"
"   border-bottom-color: rgb(255, 255, 255);\n"
"   border:2px solid rgb(202, 240, 248);\n"
"   border-radius:20px;\n"
"   border-color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(202, 240, 248);\n"
"     border:2px solid rgb(202, 240, 248);\n"
"}\n"
"    \n"
"   ")
        self.optwdw_btn_exit.setObjectName("optwdw_btn_exit")
        cs_options_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cs_options_window)
        self.statusbar.setObjectName("statusbar")
        cs_options_window.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(cs_options_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        cs_options_window.setMenuBar(self.menubar)

        self.retranslateUi(cs_options_window)
        QtCore.QMetaObject.connectSlotsByName(cs_options_window)

    def retranslateUi(self, cs_options_window):
        _translate = QtCore.QCoreApplication.translate
        cs_options_window.setWindowTitle(_translate("cs_options_window", "MainWindow"))
        self.csoptwdw_lbl_heading.setText(_translate("cs_options_window", "Hello"))
        self.optwdw_btn_transfer.setText(_translate("cs_options_window", "Transfer Money"))
        self.optwdw_btn_banktr.setText(_translate("cs_options_window", "Bank Transactions"))
        self.optwdw_btn_editinf.setText(_translate("cs_options_window", "Edit Information"))
        self.optwdw_btn_bankstt.setText(_translate("cs_options_window", "Bank Statement"))
        self.optwdw_btn_back.setText(_translate("cs_options_window", "Back"))
        self.optwdw_btn_exit.setText(_translate("cs_options_window", "Exit"))
