# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Documents/GitHub/BankingApp_SQL/admin_edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_infoEdit_window(object):
    def setupUi(self, Admin_infoEdit_window):
        Admin_infoEdit_window.setObjectName("Admin_infoEdit_window")
        Admin_infoEdit_window.resize(600, 700)
        Admin_infoEdit_window.setMinimumSize(QtCore.QSize(600, 700))
        Admin_infoEdit_window.setMaximumSize(QtCore.QSize(600, 700))
        Admin_infoEdit_window.setStyleSheet("background-color: rgb(241, 242, 248);")
        self.centralwidget = QtWidgets.QWidget(Admin_infoEdit_window)
        self.centralwidget.setObjectName("centralwidget")
        self.adeditwdw_btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.adeditwdw_btn_save.setGeometry(QtCore.QRect(340, 580, 180, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_btn_save.setFont(font)
        self.adeditwdw_btn_save.setStyleSheet("QPushButton{\n"
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
        self.adeditwdw_btn_save.setIcon(icon)
        self.adeditwdw_btn_save.setIconSize(QtCore.QSize(40, 40))
        self.adeditwdw_btn_save.setObjectName("adeditwdw_btn_save")
        self.ad_edit_wdw_warn_lbl = QtWidgets.QLabel(self.centralwidget)
        self.ad_edit_wdw_warn_lbl.setGeometry(QtCore.QRect(70, 520, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ad_edit_wdw_warn_lbl.setFont(font)
        self.ad_edit_wdw_warn_lbl.setText("")
        self.ad_edit_wdw_warn_lbl.setObjectName("ad_edit_wdw_warn_lbl")
        self.adeditwdw_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.adeditwdw_btn_back.setGeometry(QtCore.QRect(90, 580, 180, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_btn_back.setFont(font)
        self.adeditwdw_btn_back.setStyleSheet("QPushButton{\n"
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
        icon1.addPixmap(QtGui.QPixmap("icons/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adeditwdw_btn_back.setIcon(icon1)
        self.adeditwdw_btn_back.setIconSize(QtCore.QSize(40, 40))
        self.adeditwdw_btn_back.setObjectName("adeditwdw_btn_back")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 230, 491, 271))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.ad_edit_wdw_cs_name_lnedit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ad_edit_wdw_cs_name_lnedit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_edit_wdw_cs_name_lnedit.sizePolicy().hasHeightForWidth())
        self.ad_edit_wdw_cs_name_lnedit.setSizePolicy(sizePolicy)
        self.ad_edit_wdw_cs_name_lnedit.setMinimumSize(QtCore.QSize(250, 50))
        self.ad_edit_wdw_cs_name_lnedit.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ad_edit_wdw_cs_name_lnedit.setFont(font)
        self.ad_edit_wdw_cs_name_lnedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad_edit_wdw_cs_name_lnedit.setObjectName("ad_edit_wdw_cs_name_lnedit")
        self.gridLayout_2.addWidget(self.ad_edit_wdw_cs_name_lnedit, 0, 2, 1, 1)
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
        self.adeditwdw_lbl_password = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.adeditwdw_lbl_password.setMinimumSize(QtCore.QSize(110, 50))
        self.adeditwdw_lbl_password.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_lbl_password.setFont(font)
        self.adeditwdw_lbl_password.setStyleSheet("color: rgb(0, 51, 51);")
        self.adeditwdw_lbl_password.setObjectName("adeditwdw_lbl_password")
        self.gridLayout_2.addWidget(self.adeditwdw_lbl_password, 2, 0, 1, 1)
        self.adeditwdw_lbl_email = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.adeditwdw_lbl_email.setMinimumSize(QtCore.QSize(110, 50))
        self.adeditwdw_lbl_email.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_lbl_email.setFont(font)
        self.adeditwdw_lbl_email.setStyleSheet("color: rgb(0, 51, 51);")
        self.adeditwdw_lbl_email.setObjectName("adeditwdw_lbl_email")
        self.gridLayout_2.addWidget(self.adeditwdw_lbl_email, 1, 0, 1, 1)
        self.ad_edit_wdw_cs_pw_lnedit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ad_edit_wdw_cs_pw_lnedit.setMinimumSize(QtCore.QSize(0, 50))
        self.ad_edit_wdw_cs_pw_lnedit.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ad_edit_wdw_cs_pw_lnedit.setFont(font)
        self.ad_edit_wdw_cs_pw_lnedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad_edit_wdw_cs_pw_lnedit.setObjectName("ad_edit_wdw_cs_pw_lnedit")
        self.gridLayout_2.addWidget(self.ad_edit_wdw_cs_pw_lnedit, 2, 2, 1, 1)
        self.adeditwdw_lbl_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.adeditwdw_lbl_name.setMinimumSize(QtCore.QSize(110, 50))
        self.adeditwdw_lbl_name.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_lbl_name.setFont(font)
        self.adeditwdw_lbl_name.setStyleSheet("color: rgb(0, 51, 51);")
        self.adeditwdw_lbl_name.setObjectName("adeditwdw_lbl_name")
        self.gridLayout_2.addWidget(self.adeditwdw_lbl_name, 0, 0, 1, 1)
        self.ad_edit_wdw_cs_email_lnedit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ad_edit_wdw_cs_email_lnedit.setMinimumSize(QtCore.QSize(0, 50))
        self.ad_edit_wdw_cs_email_lnedit.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ad_edit_wdw_cs_email_lnedit.setFont(font)
        self.ad_edit_wdw_cs_email_lnedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad_edit_wdw_cs_email_lnedit.setObjectName("ad_edit_wdw_cs_email_lnedit")
        self.gridLayout_2.addWidget(self.ad_edit_wdw_cs_email_lnedit, 1, 2, 1, 1)
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
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 60, 491, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.adeditwdw_lbl_heading = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.adeditwdw_lbl_heading.setMinimumSize(QtCore.QSize(110, 50))
        self.adeditwdw_lbl_heading.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_lbl_heading.setFont(font)
        self.adeditwdw_lbl_heading.setStyleSheet("color: rgb(0, 51, 51);")
        self.adeditwdw_lbl_heading.setObjectName("adeditwdw_lbl_heading")
        self.gridLayout_4.addWidget(self.adeditwdw_lbl_heading, 0, 0, 1, 1)
        self.lbl_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lbl_9.setMinimumSize(QtCore.QSize(20, 50))
        self.lbl_9.setMaximumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_9.setFont(font)
        self.lbl_9.setStyleSheet("color: rgb(0, 51, 51);")
        self.lbl_9.setObjectName("lbl_9")
        self.gridLayout_4.addWidget(self.lbl_9, 0, 1, 1, 1)
        self.ad_edit_wdw_cs_id_lnedit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ad_edit_wdw_cs_id_lnedit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_edit_wdw_cs_id_lnedit.sizePolicy().hasHeightForWidth())
        self.ad_edit_wdw_cs_id_lnedit.setSizePolicy(sizePolicy)
        self.ad_edit_wdw_cs_id_lnedit.setMinimumSize(QtCore.QSize(250, 50))
        self.ad_edit_wdw_cs_id_lnedit.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ad_edit_wdw_cs_id_lnedit.setFont(font)
        self.ad_edit_wdw_cs_id_lnedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ad_edit_wdw_cs_id_lnedit.setObjectName("ad_edit_wdw_cs_id_lnedit")
        self.gridLayout_4.addWidget(self.ad_edit_wdw_cs_id_lnedit, 0, 2, 1, 1)
        self.adeditwdw_btn_getinfo = QtWidgets.QPushButton(self.centralwidget)
        self.adeditwdw_btn_getinfo.setGeometry(QtCore.QRect(160, 150, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.adeditwdw_btn_getinfo.setFont(font)
        self.adeditwdw_btn_getinfo.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adeditwdw_btn_getinfo.setIcon(icon2)
        self.adeditwdw_btn_getinfo.setIconSize(QtCore.QSize(40, 40))
        self.adeditwdw_btn_getinfo.setObjectName("adeditwdw_btn_getinfo")
        Admin_infoEdit_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Admin_infoEdit_window)
        self.statusbar.setObjectName("statusbar")
        Admin_infoEdit_window.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_infoEdit_window)
        self.ad_edit_wdw_cs_id_lnedit.returnPressed.connect(self.adeditwdw_btn_getinfo.click) # type: ignore
        self.ad_edit_wdw_cs_name_lnedit.returnPressed.connect(self.adeditwdw_btn_save.click) # type: ignore
        self.ad_edit_wdw_cs_email_lnedit.returnPressed.connect(self.adeditwdw_btn_save.click) # type: ignore
        self.ad_edit_wdw_cs_pw_lnedit.returnPressed.connect(self.adeditwdw_btn_save.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Admin_infoEdit_window)

    def retranslateUi(self, Admin_infoEdit_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_infoEdit_window.setWindowTitle(_translate("Admin_infoEdit_window", "MainWindow"))
        self.adeditwdw_btn_save.setText(_translate("Admin_infoEdit_window", "  SAVE"))
        self.adeditwdw_btn_back.setText(_translate("Admin_infoEdit_window", "  BACK"))
        self.lbl.setText(_translate("Admin_infoEdit_window", ":"))
        self.lbl_3.setText(_translate("Admin_infoEdit_window", ":"))
        self.adeditwdw_lbl_password.setText(_translate("Admin_infoEdit_window", "Password"))
        self.adeditwdw_lbl_email.setText(_translate("Admin_infoEdit_window", "Email"))
        self.adeditwdw_lbl_name.setText(_translate("Admin_infoEdit_window", "Name"))
        self.lbl_2.setText(_translate("Admin_infoEdit_window", ":"))
        self.adeditwdw_lbl_heading.setText(_translate("Admin_infoEdit_window", "Customer ID"))
        self.lbl_9.setText(_translate("Admin_infoEdit_window", ":"))
        self.adeditwdw_btn_getinfo.setText(_translate("Admin_infoEdit_window", "  Get Customer Information"))
