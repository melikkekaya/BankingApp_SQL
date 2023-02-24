# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\musab\OneDrive\Belgeler\GitHub\BankingApp_SQL\admin_statements_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_statements_window(object):
    def setupUi(self, admin_statements_window):
        admin_statements_window.setObjectName("admin_statements_window")
        admin_statements_window.setWindowModality(QtCore.Qt.ApplicationModal)
        admin_statements_window.resize(600, 700)
        admin_statements_window.setMinimumSize(QtCore.QSize(600, 700))
        admin_statements_window.setMaximumSize(QtCore.QSize(600, 700))
        admin_statements_window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        admin_statements_window.setAcceptDrops(False)
        admin_statements_window.setStyleSheet("background-color: rgb(5, 130, 202);")
        admin_statements_window.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(admin_statements_window)
        self.centralwidget.setObjectName("centralwidget")
        self.ADstatementswdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_heading.setGeometry(QtCore.QRect(30, 20, 541, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_lbl_heading.setFont(font)
        self.ADstatementswdw_lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.ADstatementswdw_lbl_heading.setObjectName("ADstatementswdw_lbl_heading")
        self.ADstatementswdw_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.ADstatementswdw_btn_back.setEnabled(True)
        self.ADstatementswdw_btn_back.setGeometry(QtCore.QRect(220, 540, 180, 70))
        self.ADstatementswdw_btn_back.setMinimumSize(QtCore.QSize(180, 70))
        self.ADstatementswdw_btn_back.setMaximumSize(QtCore.QSize(180, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ADstatementswdw_btn_back.setFont(font)
        self.ADstatementswdw_btn_back.setStyleSheet("QPushButton {\n"
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
        self.ADstatementswdw_btn_back.setObjectName("ADstatementswdw_btn_back")
        self.ADstatementswdw_lbl_filter = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter.setGeometry(QtCore.QRect(40, 80, 91, 41))
        self.ADstatementswdw_lbl_filter.setObjectName("ADstatementswdw_lbl_filter")
        self.ADstatementswdw_btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.ADstatementswdw_btn_search.setGeometry(QtCore.QRect(40, 290, 75, 23))
        self.ADstatementswdw_btn_search.setObjectName("ADstatementswdw_btn_search")
        self.ADstatementswdw_lbl_filter_date = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter_date.setGeometry(QtCore.QRect(40, 130, 47, 14))
        self.ADstatementswdw_lbl_filter_date.setObjectName("ADstatementswdw_lbl_filter_date")
        self.ADstatementswdw_lbl_filter_date_Ttype = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter_date_Ttype.setGeometry(QtCore.QRect(40, 250, 101, 16))
        self.ADstatementswdw_lbl_filter_date_Ttype.setObjectName("ADstatementswdw_lbl_filter_date_Ttype")
        self.ADstatementswdw_lbl_filter_amount = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter_amount.setGeometry(QtCore.QRect(40, 220, 47, 14))
        self.ADstatementswdw_lbl_filter_amount.setObjectName("ADstatementswdw_lbl_filter_amount")
        self.ADstatementswdw_lbl_filter_name = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter_name.setGeometry(QtCore.QRect(40, 190, 47, 14))
        self.ADstatementswdw_lbl_filter_name.setObjectName("ADstatementswdw_lbl_filter_name")
        self.ADstatementswdw_lbl_filter_csid = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_filter_csid.setGeometry(QtCore.QRect(40, 160, 81, 16))
        self.ADstatementswdw_lbl_filter_csid.setObjectName("ADstatementswdw_lbl_filter_csid")
        self.ADstatementswdw_dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.ADstatementswdw_dateTimeEdit_start.setGeometry(QtCore.QRect(130, 130, 121, 22))
        self.ADstatementswdw_dateTimeEdit_start.setObjectName("ADstatementswdw_dateTimeEdit_start")
        self.ADstatementswdw_dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.ADstatementswdw_dateTimeEdit_end.setGeometry(QtCore.QRect(300, 130, 121, 22))
        self.ADstatementswdw_dateTimeEdit_end.setObjectName("ADstatementswdw_dateTimeEdit_end")
        self.ADstatementswdw_lbl_start = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_start.setGeometry(QtCore.QRect(90, 130, 31, 16))
        self.ADstatementswdw_lbl_start.setObjectName("ADstatementswdw_lbl_start")
        self.ADstatementswdw_lbl_end = QtWidgets.QLabel(self.centralwidget)
        self.ADstatementswdw_lbl_end.setGeometry(QtCore.QRect(260, 130, 31, 16))
        self.ADstatementswdw_lbl_end.setObjectName("ADstatementswdw_lbl_end")
        self.ADstatementswdw_lnedit_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.ADstatementswdw_lnedit_amount.setGeometry(QtCore.QRect(100, 220, 113, 20))
        self.ADstatementswdw_lnedit_amount.setObjectName("ADstatementswdw_lnedit_amount")
        self.ADstatementswdw_combobox_Ttype = QtWidgets.QComboBox(self.centralwidget)
        self.ADstatementswdw_combobox_Ttype.setGeometry(QtCore.QRect(140, 250, 91, 22))
        self.ADstatementswdw_combobox_Ttype.setObjectName("ADstatementswdw_combobox_Ttype")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_combobox_Ttype.addItem("")
        self.ADstatementswdw_lnedit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.ADstatementswdw_lnedit_name.setGeometry(QtCore.QRect(100, 190, 113, 20))
        self.ADstatementswdw_lnedit_name.setObjectName("ADstatementswdw_lnedit_name")
        self.ADstatementswdw_lnedit_csid = QtWidgets.QLineEdit(self.centralwidget)
        self.ADstatementswdw_lnedit_csid.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.ADstatementswdw_lnedit_csid.setObjectName("ADstatementswdw_lnedit_csid")
        self.ADstatementswdw_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.ADstatementswdw_tableWidget.setGeometry(QtCore.QRect(40, 330, 531, 192))
        self.ADstatementswdw_tableWidget.setObjectName("ADstatementswdw_tableWidget")
        self.ADstatementswdw_tableWidget.setColumnCount(8)
        self.ADstatementswdw_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ADstatementswdw_tableWidget.setHorizontalHeaderItem(7, item)
        admin_statements_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin_statements_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        admin_statements_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin_statements_window)
        self.statusbar.setObjectName("statusbar")
        admin_statements_window.setStatusBar(self.statusbar)

        self.retranslateUi(admin_statements_window)
        QtCore.QMetaObject.connectSlotsByName(admin_statements_window)

    def retranslateUi(self, admin_statements_window):
        _translate = QtCore.QCoreApplication.translate
        admin_statements_window.setWindowTitle(_translate("admin_statements_window", "Customer Bank Statement"))
        self.ADstatementswdw_lbl_heading.setText(_translate("admin_statements_window", "Statements"))
        self.ADstatementswdw_btn_back.setText(_translate("admin_statements_window", "Back"))
        self.ADstatementswdw_lbl_filter.setText(_translate("admin_statements_window", "Filtering Options:"))
        self.ADstatementswdw_btn_search.setText(_translate("admin_statements_window", "Search"))
        self.ADstatementswdw_lbl_filter_date.setText(_translate("admin_statements_window", "Date:"))
        self.ADstatementswdw_lbl_filter_date_Ttype.setText(_translate("admin_statements_window", "Transaction Type:"))
        self.ADstatementswdw_lbl_filter_amount.setText(_translate("admin_statements_window", "Amount:"))
        self.ADstatementswdw_lbl_filter_name.setText(_translate("admin_statements_window", "Name:"))
        self.ADstatementswdw_lbl_filter_csid.setText(_translate("admin_statements_window", "Customer ID:"))
        self.ADstatementswdw_lbl_start.setText(_translate("admin_statements_window", "Start:"))
        self.ADstatementswdw_lbl_end.setText(_translate("admin_statements_window", "End:"))
        self.ADstatementswdw_combobox_Ttype.setItemText(0, _translate("admin_statements_window", "Deposit"))
        self.ADstatementswdw_combobox_Ttype.setItemText(1, _translate("admin_statements_window", "Withdraw"))
        self.ADstatementswdw_combobox_Ttype.setItemText(2, _translate("admin_statements_window", "Bank Transfer"))
        self.ADstatementswdw_combobox_Ttype.setItemText(3, _translate("admin_statements_window", "EFT"))
        self.ADstatementswdw_combobox_Ttype.setItemText(4, _translate("admin_statements_window", "Login"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("admin_statements_window", "Customer ID"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("admin_statements_window", "Name"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("admin_statements_window", "Email"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("admin_statements_window", "Amount"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("admin_statements_window", "Transaction Type"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("admin_statements_window", "Date"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("admin_statements_window", "Receiver/Sender ID"))
        item = self.ADstatementswdw_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("admin_statements_window", "Balance"))
