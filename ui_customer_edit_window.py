# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/BankingApp_SQL/customer_edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Customer_infoEdit_window(object):
    def setupUi(self, Customer_infoEdit_window):
        Customer_infoEdit_window.setObjectName("Customer_infoEdit_window")
        Customer_infoEdit_window.resize(600, 700)
        Customer_infoEdit_window.setStyleSheet("background-color: rgb(241, 242, 248);")
        self.centralwidget = QtWidgets.QWidget(Customer_infoEdit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.cseditwdw_lbl_showname = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_lbl_showname.setGeometry(QtCore.QRect(90, 30, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_showname.setFont(font)
        self.cseditwdw_lbl_showname.setStyleSheet("color: rgb(0, 51, 51);")
        self.cseditwdw_lbl_showname.setText("")
        self.cseditwdw_lbl_showname.setObjectName("cseditwdw_lbl_showname")
        self.cseditwdw_btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.cseditwdw_btn_save.setGeometry(QtCore.QRect(330, 610, 180, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_btn_save.setFont(font)
        self.cseditwdw_btn_save.setStyleSheet("QPushButton{\n"
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
        icon.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cseditwdw_btn_save.setIcon(icon)
        self.cseditwdw_btn_save.setIconSize(QtCore.QSize(40, 40))
        self.cseditwdw_btn_save.setObjectName("cseditwdw_btn_save")
        self.cseditwdw_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.cseditwdw_btn_back.setGeometry(QtCore.QRect(120, 610, 180, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_btn_back.setFont(font)
        self.cseditwdw_btn_back.setStyleSheet("QPushButton{\n"
"color: rgb(39, 82, 97);\n"
"background-color: rgb(187, 207, 237);\n"
"border:2px solid rgb(123, 169, 191);\n"
"border-radius:20px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: rgb(225, 229, 241);\n"
"     border:2px solid rgb(196, 218, 245);\n"
"}\n"
"   ")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cseditwdw_btn_back.setIcon(icon1)
        self.cseditwdw_btn_back.setIconSize(QtCore.QSize(40, 40))
        self.cseditwdw_btn_back.setObjectName("cseditwdw_btn_back")
        self.cseditwdw_label_successave = QtWidgets.QLabel(self.centralwidget)
        self.cseditwdw_label_successave.setGeometry(QtCore.QRect(80, 480, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_label_successave.setFont(font)
        self.cseditwdw_label_successave.setStyleSheet("color: rgb(255, 255, 255);")
        self.cseditwdw_label_successave.setText("")
        self.cseditwdw_label_successave.setObjectName("cseditwdw_label_successave")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 130, 451, 311))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cseditwdw_linedit_CSname_show = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.cseditwdw_linedit_CSname_show.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cseditwdw_linedit_CSname_show.sizePolicy().hasHeightForWidth())
        self.cseditwdw_linedit_CSname_show.setSizePolicy(sizePolicy)
        self.cseditwdw_linedit_CSname_show.setMinimumSize(QtCore.QSize(250, 50))
        self.cseditwdw_linedit_CSname_show.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.cseditwdw_linedit_CSname_show.setFont(font)
        self.cseditwdw_linedit_CSname_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cseditwdw_linedit_CSname_show.setObjectName("cseditwdw_linedit_CSname_show")
        self.gridLayout_2.addWidget(self.cseditwdw_linedit_CSname_show, 0, 2, 1, 1)
        self.cseditwdw_lbl_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.cseditwdw_lbl_name.setMinimumSize(QtCore.QSize(110, 50))
        self.cseditwdw_lbl_name.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_name.setFont(font)
        self.cseditwdw_lbl_name.setStyleSheet("color: rgb(0, 51, 51);")
        self.cseditwdw_lbl_name.setObjectName("cseditwdw_lbl_name")
        self.gridLayout_2.addWidget(self.cseditwdw_lbl_name, 0, 0, 1, 1)
        self.cseditwdw_lbl_email = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.cseditwdw_lbl_email.setMinimumSize(QtCore.QSize(110, 50))
        self.cseditwdw_lbl_email.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_email.setFont(font)
        self.cseditwdw_lbl_email.setStyleSheet("color: rgb(0, 51, 51);")
        self.cseditwdw_lbl_email.setObjectName("cseditwdw_lbl_email")
        self.gridLayout_2.addWidget(self.cseditwdw_lbl_email, 1, 0, 1, 1)
        self.lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl.setMinimumSize(QtCore.QSize(20, 50))
        self.lbl.setMaximumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl.setObjectName("lbl")
        self.gridLayout_2.addWidget(self.lbl, 0, 1, 1, 1)
        self.cseditwdw_linedit_CSemail_show = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.cseditwdw_linedit_CSemail_show.setMinimumSize(QtCore.QSize(0, 50))
        self.cseditwdw_linedit_CSemail_show.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.cseditwdw_linedit_CSemail_show.setFont(font)
        self.cseditwdw_linedit_CSemail_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cseditwdw_linedit_CSemail_show.setObjectName("cseditwdw_linedit_CSemail_show")
        self.gridLayout_2.addWidget(self.cseditwdw_linedit_CSemail_show, 1, 2, 1, 1)
        self.cseditwdw_lbl_password = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.cseditwdw_lbl_password.setMinimumSize(QtCore.QSize(110, 50))
        self.cseditwdw_lbl_password.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cseditwdw_lbl_password.setFont(font)
        self.cseditwdw_lbl_password.setStyleSheet("color: rgb(0, 51, 51);")
        self.cseditwdw_lbl_password.setObjectName("cseditwdw_lbl_password")
        self.gridLayout_2.addWidget(self.cseditwdw_lbl_password, 2, 0, 1, 1)
        self.cseditwdw_linedit_CSpassword_show = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.cseditwdw_linedit_CSpassword_show.setMinimumSize(QtCore.QSize(0, 50))
        self.cseditwdw_linedit_CSpassword_show.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.cseditwdw_linedit_CSpassword_show.setFont(font)
        self.cseditwdw_linedit_CSpassword_show.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cseditwdw_linedit_CSpassword_show.setObjectName("cseditwdw_linedit_CSpassword_show")
        self.gridLayout_2.addWidget(self.cseditwdw_linedit_CSpassword_show, 2, 2, 1, 1)
        self.lbl_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_3.setMinimumSize(QtCore.QSize(20, 50))
        self.lbl_3.setMaximumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_3.setFont(font)
        self.lbl_3.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout_2.addWidget(self.lbl_3, 1, 1, 1, 1)
        self.lbl_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_2.setMinimumSize(QtCore.QSize(20, 50))
        self.lbl_2.setMaximumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_2.setFont(font)
        self.lbl_2.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout_2.addWidget(self.lbl_2, 2, 1, 1, 1)
        Customer_infoEdit_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Customer_infoEdit_window)
        self.statusbar.setObjectName("statusbar")
        Customer_infoEdit_window.setStatusBar(self.statusbar)

        self.retranslateUi(Customer_infoEdit_window)
        QtCore.QMetaObject.connectSlotsByName(Customer_infoEdit_window)

    def retranslateUi(self, Customer_infoEdit_window):
        _translate = QtCore.QCoreApplication.translate
        Customer_infoEdit_window.setWindowTitle(_translate("Customer_infoEdit_window", "MainWindow"))
        self.cseditwdw_btn_save.setText(_translate("Customer_infoEdit_window", "  SAVE"))
        self.cseditwdw_btn_back.setText(_translate("Customer_infoEdit_window", "  BACK"))
        self.cseditwdw_lbl_name.setText(_translate("Customer_infoEdit_window", "Name"))
        self.cseditwdw_lbl_email.setText(_translate("Customer_infoEdit_window", "Email"))
        self.lbl.setText(_translate("Customer_infoEdit_window", ":"))
        self.cseditwdw_lbl_password.setText(_translate("Customer_infoEdit_window", "Password"))
        self.lbl_3.setText(_translate("Customer_infoEdit_window", ":"))
        self.lbl_2.setText(_translate("Customer_infoEdit_window", ":"))
