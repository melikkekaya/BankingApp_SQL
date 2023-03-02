from PyQt5.QtWidgets import *
import psycopg2, sys
import hashlib

from Ui_main_window import *
from Ui_customer_login_window import *
from Ui_customer_main_window import *
from Ui_admin_createCS_window import *
from Ui_admin_window import *
from Ui_customer_statements_window import *
from Ui_cs_options_window import *
from Ui_customer_transfer_window import *
from Ui_admin_options_window import *
from Ui_admin_edit_window import *
from Ui_customer_edit_window import *
from Ui_admin_statements_window import *

class Main_Window(QMainWindow, Ui_open_window):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.openwdw_btn_CSLogin.clicked.connect(self.cslogin)
        self.openwdw_btn_ADLogin.clicked.connect(self.adlogin)
        self.openwdw_btn_exit.clicked.connect(self.close_w)
    def adlogin(self):
        self.admin = ADPreLogin()
        widget.addWidget(self.admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.admin.show() 
    def cslogin(self):
        self.customer = CsLogin()
        widget.addWidget(self.customer)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.customer.show() 
    def close_w(self):
        sys.exit()  

class ADPreLogin(QMainWindow, Ui_admin_window):
    def __init__(self):
        super(ADPreLogin, self).__init__()
        self.setupUi(self)
        self.adminwdw_btn_login.clicked.connect(self.adafterlogin)
        self.adminwdw_btn_returnmain.clicked.connect(self.return_back)
        self.adminwdw_btn_exit.clicked.connect(self.close_w)
    def adafterlogin(self):
        AdminID = self.adminwdw_linedit_ADid.text()
        ADpassword = self.adminwdw_linedit_ADpassword.text()
        try:    
            if len(AdminID) == 0 or len(ADpassword) == 0:
                self.adminwdw_lbl_warning.setText("Please fill the required fields!")
            else:
                conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
                cur = conn.cursor()
                cur.execute(f"SELECT admin_password FROM admin WHERE admin_id={AdminID}")
                password = cur.fetchone()[0]
                if ADpassword == password:
                    print("Successfully logged in")
                    self.admin_opt = Admin_Opt()
                    widget.addWidget(self.admin_opt)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                    self.admin_opt.show()
                    cur.close()
                    conn.commit()
                    conn.close()
                
                else:
                    self.adminwdw_lbl_warning.setText("Invalid Password!")
                    print(password)
        except:
            self.adminwdw_lbl_warning.setText("Are you sure that you are an Admin because it seems everything wrong here..")

    def return_back(self):
        main = Main_Window()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def close_w(self):
        sys.exit()  

class Admin_Opt(QMainWindow, Ui_admin_options_window):
    def __init__(self):
        super(Admin_Opt, self).__init__()
        self.setupUi(self)
        self.adminwdw_btn_createcs.clicked.connect(self.scrn_create_customer)
        self.adminwdw_btn_editinf.clicked.connect(self.scrn_edit_info)
        self.adminwdw_btn_bankstt.clicked.connect(self.scrn_statements)
        self.adminwdw_btn_logout.clicked.connect(self.return_back)
        self.adminwdw_btn_exit.clicked.connect(self.close_w)
    
    def scrn_create_customer(self):
        self.cs_create = AD_CS_create()
        widget.addWidget(self.cs_create)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.cs_create.show()
    
    def scrn_edit_info(self):
        self.ad_cs_edit = AD_CS_Edit()
        widget.addWidget(self.ad_cs_edit)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.ad_cs_edit.show()

    def scrn_statements(self):
        self.ad_statements = AD_Statements()
        widget.addWidget(self.ad_statements)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.ad_statements.show()

    def return_back(self):
        adprelogin = ADPreLogin()
        widget.addWidget(adprelogin)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def close_w(self):
        sys.exit() 

class AD_CS_create(QMainWindow, Ui_admin_CScreate_window):
    def __init__(self):
        super(AD_CS_create, self).__init__()
        self.setupUi(self)
        self.admincswdw_btn_create.clicked.connect(self.createcustomer)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_CSpassword_2.clear)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_name.clear)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_linedit_email.clear)
        self.admincswdw_btn_create.clicked.connect(self.admincswdw_spinBox_balance.clear)
        self.admincswdw_btn_returnmain.clicked.connect(self.return_back)
        self.admincswdw_btn_exit.clicked.connect(self.close_w)
    
    def hash_password(self, unhashpass):
            Password = unhashpass
            hash_object = hashlib.sha256(Password.encode('utf-8'))
            Pass_hash = hash_object.hexdigest()  
            return Pass_hash
    
    def createcustomer(self):
        Name = self.admincswdw_linedit_name.text()
        Email = self.admincswdw_linedit_email.text()
        Password = self.hash_password(self.admincswdw_linedit_CSpassword_2.text())
        CurrentBalance = int(self.admincswdw_spinBox_balance.text().split("€")[0])
        if  len(Name) == 0 or len(Email) == 0 or len(Password) == 0:
            self.admincswdw_lbl_result.setText("Please fill all the fields!")
        elif Name and Email and Password:
            conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
            cur = conn.cursor()
            cur.execute("INSERT INTO customer VALUES(%s,%s,%s,%s)",(f"{Name}", f"{Email}", f"{Password}", f"{CurrentBalance}"))
            cur.execute(f"SELECT MAX(customer_id) FROM customer")
            CustomerID = cur.fetchone()[0]
            cur.execute("INSERT INTO balance VALUES(%s,%s)",(f"{CustomerID}", f"{CurrentBalance}"))
            cur.close()
            conn.commit()
            conn.close()
            self.admincswdw_lbl_result.setText(f"New customer created:\n{CustomerID}")
    
    def return_back(self):
            ADlogin = Admin_Opt()
            widget.addWidget(ADlogin)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    def close_w(self):
        sys.exit()  

class AD_CS_Edit(QMainWindow, Ui_Admin_infoEdit_window):
    def __init__(self):
        super(AD_CS_Edit, self).__init__()
        self.setupUi(self)
        self.adeditwdw_btn_back.clicked.connect(self.return_back)
        self.adeditwdw_btn_getinfo.clicked.connect(self.get_info)
        self.adeditwdw_btn_save.clicked.connect(self.save)
    def get_info(self, csid):
        self.csid = self.ad_edit_wdw_cs_id_lnedit.text()
        
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute("SELECT customer_id FROM customer")
        a = cur.fetchall()
        try: 
            for i in a:
                if int(self.csid) == i[0]:
                    cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={self.csid}")
                    name = cur.fetchone()[0]
                    cur.execute(f"SELECT cs_email FROM customer WHERE customer_id={self.csid}")
                    email = cur.fetchone()[0]
                    cur.execute(f"SELECT cs_password FROM customer WHERE customer_id={self.csid}")
                    password = cur.fetchone()[0]
                    self.ad_edit_wdw_cs_name_lnedit.setText(name)
                    self.ad_edit_wdw_cs_email_lnedit.setText(email)
                    # self.ad_edit_wdw_cs_pw_lnedit.setText(password)  
        except:
            self.ad_edit_wdw_warn_lbl.setText("Invalid Entry!")
        cur.close()
        conn.commit()
        conn.close()
    
    def save(self):
        name = self.ad_edit_wdw_cs_name_lnedit.text()
        email =self.ad_edit_wdw_cs_email_lnedit.text()
        AD_CS_edit = AD_CS_create()           
        password = AD_CS_edit.hash_password(self.ad_edit_wdw_cs_pw_lnedit.text())

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute("UPDATE customer SET cs_name= %s ,cs_email = %s, cs_password= %s WHERE customer_id = %s",(name,email,password,self.csid))
        conn.commit()
        cur.close()
        conn.close()

        self.ad_edit_wdw_cs_name_lnedit.setText(name)
        self.ad_edit_wdw_cs_email_lnedit.setText(email)
        
        self.ad_edit_wdw_warn_lbl.setStyleSheet("color: rgb(0, 84, 147);")
        self.ad_edit_wdw_warn_lbl.setText("Successfully Saved")

    
    def return_back(self):
            AD_opt = Admin_Opt()
            widget.addWidget(AD_opt)
            widget.setCurrentIndex(widget.currentIndex()+1)

class AD_Statements(QMainWindow, Ui_admin_statements_window):
    def __init__(self):
        super(AD_Statements, self).__init__()
        self.setupUi(self)
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute("REFRESH MATERIALIZED VIEW allinformation WITH DATA")
        cur.close()
        conn.commit()
        conn.close()
        
        self.ADstatementswdw_btn_back.clicked.connect(self.return_back)
        self.ADstatementswdw_dateEdit_start.setDate(QtCore.QDateTime.currentDateTime().date().addDays(-7))
        self.ADstatementswdw_dateEdit_end.setDate(QtCore.QDateTime.currentDateTime().date())
        self.ADstatementswdw_btn_search.clicked.connect(self.search)

    def search(self):
        query = ""
        ID = ""
        amnt = ""
        nm = ""
        eml = ""
        query2 = ""
        tType = self.ADstatementswdw_combobox_Ttype.currentText() 
        CustomerID = self.ADstatementswdw_lnedit_csid.text()
        Amount = self.ADstatementswdw_lnedit_amount.text()
        Name = self.ADstatementswdw_lnedit_name.text()
        Email = self.ADstatementswdw_lnedit_email.text()
        if tType != 'All':
            if tType == 'All excl. Login':
                query2 = f" AND transaction_type != 'Login' "
            else:
                query = f" AND transaction_type = '{tType}'"
        if CustomerID:
            ID = f"customer_id = '{CustomerID}' AND "
        if Amount:
            amnt = f"transaction_amount = '{Amount}' AND "
        if Name:
            nm = f"cs_name = '{Name}' AND "
        if Email:
            eml = f"cs_na = '{Email}' AND "

        start_time = self.ADstatementswdw_dateEdit_start.date().toString("yyyy-MM-dd")
        end_time = self.ADstatementswdw_dateEdit_end.date().toString("yyyy-MM-dd 23:59:59" )
        

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor() 
        cur.execute(f"SELECT customer_id,cs_name,cs_email,transaction_amount,transaction_type,receiver_sender_id,transaction_date,current_balance FROM allinformation WHERE {ID}{amnt}{nm}{eml}transaction_date >= '{start_time}' AND transaction_date <= '{end_time}' {query2} {query}")
        list = cur.fetchall()
        self.ADstatementswdw_tableWidget.setColumnWidth(2,200)
        self.ADstatementswdw_tableWidget.setRowCount(len(list))
        row = 0
        for tr in list:
            self.ADstatementswdw_tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(tr[0])))
            self.ADstatementswdw_tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(tr[1]))
            self.ADstatementswdw_tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(tr[2]))
            self.ADstatementswdw_tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(tr[3])))
            self.ADstatementswdw_tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(tr[4]))
            self.ADstatementswdw_tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(tr[5])))
            self.ADstatementswdw_tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(tr[6])))
            self.ADstatementswdw_tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(tr[7])))
            row = row + 1
        getsum = AD_Statements.get_sum(self)
        self.ADstatementswdw_lbl_get_sum.setText(f"Sum of the balance:{getsum}")
        cur.close()
        conn.commit()
        conn.close()
    
    def get_sum(self):
        seen_ids = set()
        sum = 0
        for row in range(self.ADstatementswdw_tableWidget.rowCount()):
            id_value = self.ADstatementswdw_tableWidget.item(row, 0).text()
            balance_value = float(self.ADstatementswdw_tableWidget.item(row, 7).text())
            if id_value not in seen_ids:
                seen_ids.add(id_value)
                sum += balance_value
        # print("Sum of unique balances is: {}".format(sum))
        return sum

    
    def return_back(self):
            AD_opt = Admin_Opt()
            widget.addWidget(AD_opt)
            widget.setCurrentIndex(widget.currentIndex()+1)

class CsLogin(QMainWindow,Ui_customer_login_window):
    def __init__(self):
        super(CsLogin, self).__init__()
        self.setupUi(self)
        self.csloginwdw_btn_login.clicked.connect(self.csafterlogin)  
        self.csloginwdw_btn_returnmain.clicked.connect(self.return_back)
        self.csloginwdw_btn_exit.clicked.connect(self.close_w)

    def csafterlogin(self):
        self.CsId = self.csloginwdw_linedit_ADid.text()
        self.CsPs = self.csloginwdw_linedit_ADpassword.text() 
        if len(str(self.CsId)) == 0 or len(str(self.CsPs)) == 0:
            self.csloginwdw_lbl_warning.setText("Please fill the required fields!")
        else:
            #TODO BURAYA TRY GELECEK: YANLIŞ GİRİŞ YA DA OLMAYAN KULLANICIDA ATIYOR!!
            conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
            cur = conn.cursor() 
            cur.execute(f"SELECT cs_password FROM customer WHERE customer_id={int(self.CsId)}")
            password = cur.fetchone()[0]
            ad_CS_create = AD_CS_create ()           
            hashed_password = ad_CS_create.hash_password(self.CsPs)

            if hashed_password == password:
                # try:
                CSMain.ID = self.CsId
                CSOptions.ID = self.CsId
                CSTransfer.ID = self.CsId
                CSEdit.ID = self.CsId
                CSinfo.ID = self.CsId
                print("Successfully logged in")
                cur.execute("INSERT INTO all_transactions VALUES(%s,%s,%s)",(f"{str(self.CsId)}", 0, "Login"))
                
                # try:        #öncekinde burayı neden try bloğuna aldığımızı anlamadım 
                self.csAfter = CSOptions()
                widget.addWidget(self.csAfter)
                widget.setCurrentIndex(widget.currentIndex()+1)
                self.csAfter.show()
                cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={int(self.CsId)}")
                name = cur.fetchone()[0]
                self.csAfter.csoptwdw_lbl_showname.setText(f"Hello {name}")
                # except:
                #     print("error1")

                # self.csAfter.csmainwdw_lbl_CSname_show.setText(name)
                # self.csAfter.csmainwdw_lbl_CSID_show.setText(str(self.CsId))
                cur.close()
                conn.commit()
                conn.close()
                # except:
                #     print("error2")
            else:
                self.csloginwdw_lbl_warning.setText("Invalid ID or Password!")

    def return_back(self):
            main = Main_Window()
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def close_w(self):
        sys.exit()            

class CSOptions(QMainWindow, Ui_cs_options_window):
    def __init__(self):
        super(CSOptions, self).__init__()
        self.setupUi(self)
        self.ID

        self.optwdw_btn_banktr.clicked.connect(self.open_transactions)
        self.optwdw_btn_transfer.clicked.connect(self.open_transfer)
        self.optwdw_btn_editinf.clicked.connect(self.open_edit)
        self.optwdw_btn_bankstt.clicked.connect(self.bankstt)
        self.optwdw_btn_back.clicked.connect(self.return_back)
        self.optwdw_btn_exit.clicked.connect(self.close_w)        

    def open_transactions(self):
        self.csAfter = CSMain()
        widget.addWidget(self.csAfter)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.csAfter.show()

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={self.ID}")
        name = cur.fetchone()[0]
        self.csAfter.csmainwdw_lbl_CSname_show.setText(name)
        self.csAfter.csmainwdw_lbl_CSID_show.setText(str(self.ID))
        cur.close()
        conn.commit()
        conn.close()
    
    def open_transfer(self):
        self.csAfter = CSTransfer()
        widget.addWidget(self.csAfter)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.csAfter.show()

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={self.ID}")
        name = cur.fetchone()[0]
        self.csAfter.cstrfwdw_lbl_CSname_show.setText(name)
        self.csAfter.cstrfwdw_lbl_CSID_show.setText(str(self.ID))
        self.csAfter.cstrfwdw_radiobtn_inttrf.setChecked(True)
        cur.close()
        conn.commit()
        conn.close()
    
    def open_edit(self):
        self.csAfter = CSEdit()
        widget.addWidget(self.csAfter)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.csAfter.show()

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={self.ID}")
        name = cur.fetchone()[0]
        cur.execute(f"SELECT cs_email FROM customer WHERE customer_id={self.ID}")
        email = cur.fetchone()[0]
        cur.execute(f"SELECT cs_password FROM customer WHERE customer_id={self.ID}")
        passwordd = cur.fetchone()[0]
        
        self.csAfter.cseditwdw_linedit_CSname_show.setText(name)
        self.csAfter.cseditwdw_linedit_CSemail_show.setText(email)
        self.csAfter.cseditwdw_lbl_showname.setText(f"Hello {name}")
        # self.csAfter.cseditwdw_linedit_CSpassword_show.setText(str(passwordd))
    
        cur.close()
        conn.commit()
        conn.close()
    def bankstt(self):
        self.csAfter = CSinfo()
        widget.addWidget(self.csAfter)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.csAfter.show()

    def return_back(self):
        cslogin = CsLogin()
        widget.addWidget(cslogin)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def close_w(self):
        sys.exit()  

class CSEdit(QMainWindow, Ui_Customer_infoEdit_window):
    def __init__(self):
        super(CSEdit, self).__init__()
        self.setupUi(self)
        self.cseditwdw_btn_save.clicked.connect(self.save)
        self.cseditwdw_btn_back.clicked.connect(self.csback)

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT cs_name FROM customer")
        name = cur.fetchone()[0]
        cur.execute(f"SELECT cs_email FROM customer")
        email=cur.fetchone()[0]
        cur.execute(f"SELECT cs_password FROM customer")
        password=cur.fetchone()[0]
  
    
    
    
        cur.close()
        conn.commit()
        conn.close()  

    def save(self):
        # self.csAfter = CSEdit()
        # widget.addWidget(self.csAfter)
        # widget.setCurrentIndex(widget.currentIndex()+1)
        # self.csAfter.show()

        name1 = self.cseditwdw_linedit_CSname_show.text()
        email1 =self.cseditwdw_linedit_CSemail_show.text()
        ad_CS_edit = AD_CS_create ()           
        passwordd1 = ad_CS_edit.hash_password(self.cseditwdw_linedit_CSpassword_show.text())

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute("UPDATE customer SET cs_name= %s ,cs_email = %s, cs_password= %s WHERE customer_id = %s",(name1,email1,passwordd1,self.ID))
        conn.commit()
        cur.close()
        conn.close()

        self.cseditwdw_linedit_CSname_show.setText(name1)
        self.cseditwdw_linedit_CSemail_show.setText(email1)
        self.cseditwdw_lbl_showname.setText(f"Hello {name1}")
        # self.csAfter.cseditwdw_linedit_CSpassword_show.setText(str(passwordd1))
        #self.csAfter.csmainwdw_lbl_CSID_show.setText(str(self.ID))
        self.cseditwdw_label_successave.setStyleSheet("color: rgb(0, 84, 147);")
        self.cseditwdw_label_successave.setText("Successfully Saved")

        
       
    def csback(self):  
        cs_opt = CSOptions()
        widget.addWidget(cs_opt)
        widget.setCurrentIndex(widget.currentIndex()+1)  

class CSMain(QMainWindow, Ui_customer_main_window):
    def __init__(self):
        super(CSMain, self).__init__()
        self.setupUi(self)

        self.amount = self.csmainwdw_spinbox_money.value()
        self.ID
        
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT current_balance FROM balance WHERE customer_id={self.ID}")
        self.first_balance = cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()

        self.csmainwdw_lbl_balanceshow.setText(f"{str(self.first_balance)} €")
        self.csmainwdw_btn_getcash.clicked.connect(self.get_cash)
        self.csmainwdw_btn_deposit.clicked.connect(self.deposit)
        self.csmainwdw_btn_returnmain.clicked.connect(self.return_back)
        self.csmainwdw_btn_exit.clicked.connect(self.close_w)
        # self.csmainwdw_btn_statement.clicked.connect(self.show_statement)
        
    def take_balance(self):
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT current_balance FROM balance WHERE customer_id={self.ID}")
        self.balance = cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        
    def deposit(self):
        self.take_balance()
        try:
            if self.csmainwdw_spinbox_money.value() > 0:
                b = self.balance + self.csmainwdw_spinbox_money.value()

                conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
                cur = conn.cursor()
                cur.execute("INSERT INTO all_transactions VALUES(%s,%s,%s)",(f"{self.ID}", f"{int(self.csmainwdw_spinbox_money.value())}", "Deposit Money"))
                cur.execute("UPDATE balance SET current_balance = %s WHERE customer_id = %s", (f"{b}", f"{self.ID}"))
                cur.close()
                conn.commit()
                conn.close()
                self.csmainwdw_lbl_balanceshow.setText(f"{str(b)} €")
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                self.csmainwdw_lbl_resultmessage.setText("Successful deposit to the account")

            else:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Please enter an amount..")
        except:
            print("error3")

    def get_cash(self):
        self.take_balance()
        try: 
            if self.csmainwdw_spinbox_money.value() > 0:
                if self.balance >= self.csmainwdw_spinbox_money.value():
                    c = self.balance - self.csmainwdw_spinbox_money.value()

                    conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO all_transactions VALUES(%s,%s,%s)",(f"{self.ID}", f"{int(self.csmainwdw_spinbox_money.value())}", "Withdraw Money"))
                    cur.execute("UPDATE balance SET current_balance = %s WHERE customer_id = %s", (f"{c}", f"{self.ID}"))
                    cur.close()
                    conn.commit()
                    conn.close()
                    self.csmainwdw_lbl_balanceshow.setText(f"{str(c)} €")
                    self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                    self.csmainwdw_lbl_resultmessage.setText("Successful withdraw from the account")
               
                else:
                    self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                    self.csmainwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")

            else:
                self.csmainwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.csmainwdw_lbl_resultmessage.setText("Please enter an amount to withdraw..")
        except:
            print("error4")
        
    def return_back(self):
        csoptions = CSOptions()
        widget.addWidget(csoptions)
        widget.setCurrentIndex(widget.currentIndex()+1)
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor() 
        cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={self.ID}")
        name = cur.fetchone()[0]
        csoptions.csoptwdw_lbl_showname.setText(f"Hello {name}")
        cur.close()
        conn.commit()
        conn.close()
    
    def close_w(self):
        sys.exit()  

    # def show_statement(self):
    #     self.csstatement = CSinfo()
    #     widget.addWidget(self.csstatement)
    #     widget.setCurrentIndex(widget.currentIndex()+1)
    #     file = resource_path(f"customer_database/{self.ID}.csv")
    #     with open (file, "r") as f:
    #         reader = csv.reader(f)
    #         data = [row for row in reader]
    #         self.csstatement.csstatementwdw_tbl_statement.setRowCount(len(data)-1)
    #         self.csstatement.csstatementwdw_tbl_statement.setColumnCount(len(data[0]))
    #         for i, row in enumerate(data[1:]):
    #             for j, value in enumerate(row):
    #                 self.csstatement.csstatementwdw_tbl_statement.setItem(i, j, QTableWidgetItem(value))
    #     self.csstatement.show()
    #     self.take_balance()
    #     self.csstatement.csstatementwdw_lbl_balanceshow.setText(f"{self.balance} €")

class CSTransfer(QMainWindow, Ui_customer_transfer_window):
    def __init__(self):
        super(CSTransfer, self).__init__()
        self.setupUi(self)

        self.ID

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT current_balance FROM balance WHERE customer_id={self.ID}")
        self.first_balance = cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()

        self.cstrfwdw_lbl_balanceshow.setText(f"{str(self.first_balance)} €")

        self.cstrfwdw_btn_send.clicked.connect(self.send_money)
        # self.cstrfwdw_btn_send.clicked.connect(self.show_popup)

        self.cstrfwdw_btn_returnmain.clicked.connect(self.return_back)
        self.cstrfwdw_btn_exit.clicked.connect(self.close_w)
    
    def take_balance(self):
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor()
        cur.execute(f"SELECT current_balance FROM balance WHERE customer_id={self.ID}")
        self.balance = cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        
    def send_money(self):
        self.take_balance()
        # self.show_popup()

        if self.cstrfwdw_spinbox_money.value() > 0:
            if self.balance >= self.cstrfwdw_spinbox_money.value():
                conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
                cur = conn.cursor()
                cur.execute(f"SELECT customer_id FROM customer")
                x = cur.fetchall()
                receiver_list = [i[0] for i in x]
                # TODO önce int bankada müşteri mi sonra uzunluk sorgula
                if len(self.cstrfwdw_linedit_receivernumber.text())>0:
                    if self.cstrfwdw_radiobtn_inttrf.isChecked():
                        if int(self.cstrfwdw_linedit_receivernumber.text()) in receiver_list and int(self.cstrfwdw_linedit_receivernumber.text()) != self.ID:
                            #TODO: buraya pop-up ile bu adrese göndermek istediğinize emin misiniz?
                            receiver_id = int(self.cstrfwdw_linedit_receivernumber.text())
                            d = self.balance - self.cstrfwdw_spinbox_money.value()
                            cur.execute("INSERT INTO all_transactions VALUES(%s,%s,%s,%s)",(f"{self.ID}", f"{int(self.cstrfwdw_spinbox_money.value())}", "Internal Money Transfer", f"{receiver_id}"))
                            cur.execute("INSERT INTO all_transactions VALUES(%s,%s,%s,%s)",(f"{receiver_id}", f"{int(self.cstrfwdw_spinbox_money.value())}", "Money Received", f"{self.ID}"))
                            cur.execute("UPDATE balance SET current_balance = %s WHERE customer_id = %s", (f"{d}", f"{self.ID}"))

                            cur.execute(f"SELECT current_balance FROM balance WHERE customer_id={receiver_id}")
                            receiver_balance = cur.fetchone()[0]
                            receiver__current_balance = receiver_balance + self.cstrfwdw_spinbox_money.value()
                            cur.execute("UPDATE balance SET current_balance = %s WHERE customer_id = %s", (f"{receiver__current_balance}", f"{receiver_id}"))

                            self.cstrfwdw_lbl_balanceshow.setText(f"{str(d)} €")
                            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                            self.cstrfwdw_lbl_resultmessage.setText("Successful money transfer") # buraya adı çekilip yazılabilir to ...'s acoount şeklinde
                                                
                            cur.close()
                            conn.commit()
                            conn.close()

                        elif int(self.cstrfwdw_linedit_receivernumber.text()) == self.ID:
                            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                            self.cstrfwdw_lbl_resultmessage.setText("Receiver should be different than sender..")

                        elif len(self.cstrfwdw_linedit_receivernumber.text()) < 8:           
                                self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                                self.cstrfwdw_lbl_resultmessage.setText("Receiver number should be at least 8 characters..")

                        else:
                            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                            self.cstrfwdw_lbl_resultmessage.setText("No such receiver found in our bank..")

                    # başka bankaya
                    elif self.cstrfwdw_radiobtn_exttrf.isChecked():
                        receiver_id = int(self.cstrfwdw_linedit_receivernumber.text())
                        if len(str(receiver_id)) >= 8:
                            #TODO: buraya pop-up ile bu adrese göndermek istediğinize emin misiniz?
                            # self.show_popup()
                            # if self.show_popup(QMessageBox.Ok):
                            e = self.balance - self.cstrfwdw_spinbox_money.value()
                            conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
                            cur = conn.cursor()
                            cur.execute("INSERT INTO all_transactions VALUES(%s,%s,%s,%s)",(f"{self.ID}", f"{int(self.cstrfwdw_spinbox_money.value())}", "External Money Transfer",f"{receiver_id}"))
                            cur.execute("UPDATE balance SET current_balance = %s WHERE customer_id = %s", (f"{e}", f"{self.ID}"))
                            cur.close()
                            conn.commit()
                            conn.close()
                            self.cstrfwdw_lbl_balanceshow.setText(f"{str(e)} €")
                            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(0, 84, 147);")
                            self.cstrfwdw_lbl_resultmessage.setText("Successful money transfer")

                            # elif self.show_popup(QMessageBox.Cancel):
                            #     self.cstrfwdw_spinbox_money.cleanText()
                            #     self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                            #     self.cstrfwdw_lbl_resultmessage.setText("You've cancelled the transfer..")
                        else:
                            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                            self.cstrfwdw_lbl_resultmessage.setText("Receiver number should be at least 8 characters..")

                    else:
                        self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                        self.cstrfwdw_lbl_resultmessage.setText("Please choose a transfer method: internal or external..")

                elif len(self.cstrfwdw_linedit_receivernumber.text()) == 0:
                    self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                    self.cstrfwdw_lbl_resultmessage.setText("Please input a receiver number..")

            else:
                self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
                self.cstrfwdw_lbl_resultmessage.setText("Non-sufficient funds in the account..")

        else:
            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.cstrfwdw_lbl_resultmessage.setText("Please enter an amount to transfer..")

    def show_popup(self):
        msg = QMessageBox()
        msg.setText(f"Please confirm the money transfer to this receiver: {self.cstrfwdw_linedit_receivernumber.text()}")
        # x = msg.exec_()
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # x = msg.exec_()

        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            self.send_money()
        if returnValue == QMessageBox.Cancel:

            self.cstrfwdw_spinbox_money.cleanText()
            self.cstrfwdw_lbl_resultmessage.setStyleSheet("color: rgb(255, 0, 0);")
            self.cstrfwdw_lbl_resultmessage.setText("You've cancelled the transfer..")

    

    def return_back(self):
        csoptions = CSOptions()
        widget.addWidget(csoptions)
        widget.setCurrentIndex(widget.currentIndex()+1)
        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor() 
        cur.execute(f"SELECT cs_name FROM customer WHERE customer_id={self.ID}")
        name = cur.fetchone()[0]
        csoptions.csoptwdw_lbl_showname.setText(f"Hello {name}")
        cur.close()
        conn.commit()
        conn.close()
    
    def close_w(self):
        sys.exit()  

class CSinfo(QMainWindow, Ui_customer_statements_window):
    def __init__(self):
        super(CSinfo, self).__init__()
        self.setupUi(self)
        self.dateEdit_start.setDate(QtCore.QDateTime.currentDateTime().date().addDays(-7))
        self.dateEdit_end.setDate(QtCore.QDateTime.currentDateTime().date())
        self.CSstatementswdw_btn_back.clicked.connect(self.return_back)

        self.CSstatementswdw_btn_search.clicked.connect(self.search)
        
       
    def search(self):

        query = ""
        tType = self.CSstatements_Transection_Types_combo.currentText() 
        if tType != 'All':
            query = f" AND transaction_type = '{tType}'"

        start_time = self.dateEdit_start.date().toString("yyyy-MM-dd")
        end_time = self.dateEdit_end.date().toString("yyyy-MM-dd 23:59:59" )

        conn = psycopg2.connect("dbname=BankingApp user= postgres password=1234")
        cur = conn.cursor() 
        cur.execute(f"SELECT transaction_type,transaction_amount,transaction_date FROM all_transactions WHERE customer_id={self.ID} AND transaction_date >= '{start_time}' AND transaction_date <= '{end_time}' AND transaction_type != 'Login' {query}")
        list = cur.fetchall()
        
        self.CSstatementswdw_tableWidget.setColumnWidth(2,200)
        self.CSstatementswdw_tableWidget.setRowCount(len(list))
        row = 0
        for tr in list:
            self.CSstatementswdw_tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(tr[0]))
            self.CSstatementswdw_tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(tr[1])))
            self.CSstatementswdw_tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(tr[2])))
            row = row + 1

        cur.close()
        conn.commit()
        conn.close()

    def return_back(self):
        csoption = CSOptions()
        widget.addWidget(csoption)
        widget.setCurrentIndex(widget.currentIndex()+1)
      
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Main_Window()
    widget = QtWidgets.QStackedWidget()
    
    widget.addWidget(mainwindow)

    widget.show()

    try:
        sys.exit(app.exec_())

    except:
        print("Exiting")
    
