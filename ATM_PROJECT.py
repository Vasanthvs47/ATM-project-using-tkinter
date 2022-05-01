import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
import sqlite3
import smtplib
import random

class atm(tk.Tk):
        def __init__(self):
                tk.Tk.__init__(self)
                self.frame = None
                self.switch_frame(Greeting)
                self.iconbitmap("C:/project/atm-machine.ico")
                self.geometry('800x600')
                self.resizable(False,False)
                self.title("ATM")

        def switch_frame(self,frame):
                new = frame(self)
                if self.frame is not None:
                        self.frame.destroy()
                self.frame = new
                self.frame.pack()

        def value(self,values):
                global datas
                datas = values
                return None
        
        def data(self):
                return datas

        def new_data(self,alist):
                global new_ac
                new_ac = alist
        def send(self):
                return new_ac
        

class Greeting(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'
                def change():
                        master.switch_frame(SignIn)
               
                heading1 = tk.Label(self,text="SIMPLE ATM SOFTWARE",font=('orbitron',30,'bold'),bg='#9933ff',fg='white',width=25)
                heading1.pack(pady=5)
                
                heading2 = tk.Label(self,text="USING PYTHON",font=("orbitron",30),bg='#9933ff',fg="white")
                heading2.pack(pady=5)
                
                submit_label = tk.Label(self,text="SUBMITTED TO",font=("orbitron",20,"underline"),bg='#9933ff',fg='white')
                submit_label.pack(pady=10)
                
                mam_label = tk.Label(self,text="Ms.SABITHA.prof",font=("orbitron",15),bg='#9933ff',fg="white")
                mam_label.pack(pady=5)
                
                empty = tk.Label(self,height=5,bg='#9933ff')
                empty.pack()
                
                crew_prepared = tk.Label(self,text="PREPARED BY",font=('orbitron',20,'underline'),bg='#9933ff',fg='white')
                crew_prepared.pack(pady=5)
                
                crew = tk.Label(self,text="P.S.MOHANRAJ   V.NAKUL   E.SARAN   M.VASANTH",font=('orbitron',15),bg='#9933ff',fg='white')
                crew.pack(pady=5)
                
                empty1 = tk.Label(self,height=5,bg='#9933ff')
                empty1.pack()

                photo = tk.PhotoImage(file=r"C:\project\rose.png")
                photo1 = photo.subsample(15,15)
                
                Enter = tk.Button(self,text=" START",bg='#330066',fg='white',font=('orbitron',15),command=change,bd=5,image=photo1,compound=tk.LEFT)
                Enter.image = photo1
                Enter.pack(side="bottom",ipadx=20)

class SignIn(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'
                def check():
                        a = False
                        Ac_num = None
                        try:
                                Ac_num = int(user_entry.get())
                        except ValueError:
                                incorrect['text'] = "INVALID ACCOUNT NUMBER"
                                return None
                        password = None
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT * FROM UserData WHERE AcNum={Ac_num}")
                                alist = cursor.fetchall()
                        if alist == []:
                                incorrect['text'] = "INVALID ACCOUNT NUMBER"
                        else:
                                password = alist[0][3]
                                a = True
                        if a:
                                if password_entry.get() == '':
                                        incorrect['text'] = "ENTER YOUR NAME \n AND PASSWORD"
                                elif password_entry.get() == password:
                                        master.value(alist[0])
                                        master.switch_frame(MainPage)
                                else:
                                        incorrect['text'] = "Incorrect password "
                sub = tk.PhotoImage(file=r"C:\project\sub.png")
                sub_photo = sub.subsample(20,20)

                for1 = tk.PhotoImage(file=r"C:\project\forgot.png")
                for_photo = for1.subsample(20,20)

                add = tk.PhotoImage(file=r"C:\project\AddUser.png")
                add_photo = add.subsample(20,20)

                del1 = tk.PhotoImage(file=r"C:\project\DeleteUser.png")
                del_photo = del1.subsample(20,20)
                
                heading = tk.Label(self,text="Member Login",font=("orbitron",30),bg='#9933ff',fg='white')
                heading.pack(pady=10)
                
                user_name = tk.Label(self,text="ACCOUNT NUMBER: ",font='orbitron',bg='#9933ff',fg='white')
                user_name.pack(anchor='w',pady=5)
                
                user_entry = tk.Entry(self,width=20)
                user_entry.focus()
                user_entry.pack(ipadx=120,pady=5,ipady=5)
                
                password_label = tk.Label(self,text="Password: ",font="orbitron",bg='#9933ff',fg="white")
                password_label.pack(anchor='w',pady=5)
                
                password_entry = tk.Entry(self,show="X")
                password_entry.pack(ipadx=120,pady=5,ipady=5)

                frame1 = tk.Frame(self,bg='#9933ff')
                frame1.pack(ipady=3,pady=10)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)
                
                sumbit_button = tk.Button(frame1, text="  SUBMIT",font='orbitron',bd=5,bg='#330066',fg='white',command=check,image=sub_photo,compound=tk.LEFT)
                sumbit_button.image = sub_photo
                sumbit_button.pack(ipady=3,ipadx=25,side='left',padx=3)

                incorrect = tk.Label(self,text="",bg='#9933ff',fg='white',font='orbitron',width=25,height=3)
                incorrect.pack()

                empty_label = tk.Label(self,bg='#9933ff')
                empty_label.pack()

                new_account = tk.Button(self,text="  CREATE NEW ACCOUNT",font='orbitron',bg='#330066',fg='white',bd=5,command=lambda:master.switch_frame(AccountCreation),
                                        image=add_photo,compound=tk.LEFT)
                new_account.image = add_photo
                new_account.pack(ipadx=30,pady=10,ipady=3)

                delete_account = tk.Button(self,text="  DELETE ACCOUNT",font='orbitron',bg='#330066',fg='white',bd=5,command=lambda:master.switch_frame(DeleteAccount),
                                           image=del_photo,compound=tk.LEFT)
                delete_account.image = del_photo
                delete_account.pack(ipadx=55,pady=10,ipady=3)

                change_password = tk.Button(frame1,text=f"  FORGET",font='orbitron',bg='#330066',fg='white',bd=5,command=lambda:master.switch_frame(ChangePassword),
                                            image=for_photo,compound=tk.LEFT)
                change_password.image = for_photo
                change_password.pack(ipady=3,side='right',ipadx=25)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(Greeting),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=105,pady=10)
        
                
class MainPage(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master ['bg'] = '#9933ff'
                def Deposit():
                        master.switch_frame(DepositPage)
                def quit_page():
                        master.switch_frame(SignIn)
                def Balance():
                        master.switch_frame(BalanceEnquiryPage)
                def Withdraw():
                        master.switch_frame(WithdrawPage)
                def Transaction():
                        master.switch_frame(TransactionPage)
                name = master.data()[0]

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2,text=f"ACCOUNT HOLDER NAME: {name}",fg='white',font=('orbitron',15))
                empty_label.pack(fill="x",pady=5)

                photo = tk.PhotoImage(file=r"C:\project\deposit.png")
                photo1 = photo.subsample(3,3)

                balance_photo = tk.PhotoImage(file=r"C:\project\purse.png")
                balance_photo1 = balance_photo.subsample(20,20)

                with_p = tk.PhotoImage(file=r"C:\project\withdrawal.png")
                with_photo = with_p.subsample(15,15)

                tran_po = tk.PhotoImage(file=r"C:\project\transaction.png")
                tran_photo = tran_po.subsample(20,20)
                
                deposit_button = tk.Button(self,text="  DEPOSIT",font=("orbitron",15),bg='#330066',fg="white",command=Deposit,bd=5,image=photo1,compound=tk.LEFT)
                deposit_button.image = photo1
                deposit_button.pack(ipadx=90,pady=15,ipady=5)

                balance_button = tk.Button(self,text="  BALANCE ENQUIRY",font=("orbitron",15),bg='#330066',fg='white',command=Balance,bd=5,
                                           image=balance_photo1,compound=tk.LEFT)
                balance_button.image = balance_photo1
                balance_button.pack(ipadx=25,pady=15,ipady=5)

                withdraw_button = tk.Button(self,text="  WITHDRAW",font=("orbitron",15),bg='#330066',fg='white',command=Withdraw,bd=5,
                                            image=with_photo,compound=tk.LEFT)
                withdraw_button.image = with_photo
                withdraw_button.pack(ipadx=65,pady=15,ipady=5)

                transfer_button = tk.Button(self,text="  MONEY TRANSFER",font=("orbitron",15),bg='#330066',fg='white',command=Transaction,bd=5,
                                            image=tran_photo,compound=tk.LEFT)
                transfer_button.image = tran_photo
                transfer_button.pack(ipadx=30,pady=15,ipady=5)

                quit1 = tk.PhotoImage(file=r"C:\project\power.png")
                quit2 = quit1.subsample(20,20)
                
                quit_button = tk.Button(self,text="  QUIT",font=('orbitron',12),bg="#330066",fg="white",width=5,command=quit_page,bd=5,
                                        image=quit2,compound=tk.LEFT)
                quit_button.image = quit2
                quit_button.pack(ipadx=60,pady=15,ipady=5)

                
class DepositPage(tk.Frame):
        def __init__(self,root):
                tk.Frame.__init__(self,root,bg='#9933ff')
                self.root = root
                self.root['bg'] = '#9933ff'

                def adding():
                        alist = root.data()
                        AccNum = list(alist)[4]
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Amount FROM UserData WHERE AcNum = {AccNum}")
                                money =cursor.fetchall()[0][0]
                        amount = amount_entry.get()
                        try:
                                if amount == "":
                                        info_label['text'] = "ENTER THE AMOUNT FIRST"
                                elif int(amount) > 0:
                                        money += int(amount)
                                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                                cursor = connection.cursor()
                                                cursor.execute(f"UPDATE UserData SET Amount = {money} WHERE AcNum = {AccNum}")
                                                info_label['text'] = "MONEY ADDED SUCCESSUFFLY"
                                                
                                                
                                else:
                                        info_label['text'] = 'ENTER A VALID NUMBER'
                        except ValueError:
                                info_label['text'] = "DONOT ENTER LETTERS"
                def back():
                        self.root.switch_frame(MainPage)
                def quit_page():
                        root.switch_frame(SignIn)
                name = root.data()[0]
                        
                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2,text=f"ACCOUNT HOLDER NAME: {name}",fg='white',font=('orbitron',15))
                empty_label.pack(fill="x",pady=5)

                amount_label = tk.Label(self,text="DEPOSIT AMOUNT:",bg='#9933ff',fg='white',font=('orbitron',15),width=15)
                amount_label.pack(pady=10,anchor='w',padx=30)

                amount_entry = tk.Entry(self,width=50)
                amount_entry.focus()
                amount_entry.pack(ipadx=15,pady=10,ipady=5)

                dep = tk.PhotoImage(file=r"C:\project\deposit1.png")
                dep_photo = dep.subsample(20,20)

                add_button = tk.Button(self,text="  DEPOSIT",bg='#330066',fg='white',font=('orbitron',15),width=15,command=adding,bd=5,
                                       image=dep_photo,compound=tk.LEFT)
                add_button.image = dep_photo
                add_button.pack(ipadx=150,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:root.switch_frame(MainPage),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                info_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15))
                info_label.pack()



class BalanceEnquiryPage(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,bg='#9933ff')
                master['bg'] = '#9933ff'
                
                data = master.data()
                name = data[0]
                acnum = data[4]
                with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Amount FROM UserData WHERE AcNum = {acnum}")
                                money =cursor.fetchall()[0][0]
                def refresh():
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Amount FROM UserData WHERE Acnum = {acnum}")
                                money =cursor.fetchall()[0][0]
                        balance_label['text'] = f"CURRENT BALANCE IS {money} RUPEES"
                                        
                
                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)
                
                empty_label = tk.Label(self,bg='#9933ff',height=2,text=f"ACCOUNT HOLDER NAME: {name} ",fg='white',font=('orbitron',15))
                empty_label.pack(fill="x",pady=5)
                
                balance_label = tk.Label(self,text=f"CURRENT BALANCE IS {money} RUPEES",bg='#9933ff',fg='white',font=('orbitron',15))
                balance_label.pack(pady=20)

                ref = tk.PhotoImage(file=r"C:\project\refresh.png")
                ref_photo = ref.subsample(20,20)

                refresh_button = tk.Button(self,text="  REFRESH",font=('orbitron',15),bg="#330066",fg="white",width=20,bd=5,command=refresh,
                                           image=ref_photo,compound=tk.LEFT)
                refresh_button.image = ref_photo
                refresh_button.pack(ipadx=140,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(MainPage),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)
                

class WithdrawPage(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'
                def sub():
                        alist = master.data()
                        AccNum = list(alist)[4]
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Amount FROM UserData WHERE AcNum = {AccNum}")
                                money =cursor.fetchall()[0][0]
                        amount = amount_entry.get()
                        try:
                                if amount == "":
                                        info_label['text'] = "ENTER THE AMOUNT FIRST"
                                        return
                                elif int(amount) > money:
                                        info_label['text'] = "MORE THAN YOUR \nACCOUNT BALANCE"
                                        return
                                elif int(amount) > 0:
                                        money -= int(amount)
                                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                                cursor = connection.cursor()
                                                cursor.execute(f"UPDATE UserData SET Amount = {money} WHERE AcNum = {AccNum}")
                                                info_label['text'] = "Money Withdrawn Successfully"
                                                
                                                
                                else:
                                        info_label['text'] = 'ENTER A VALID NUMBER'
                        except ValueError:
                                info_label['text'] = "DONOT ENTER LETTERS"
                def back():
                        master.switch_frame(MainPage)
                def quit_page():
                        master.switch_frame(SignIn)
                name = master.data()[0]
                        
                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2,text=f"ACCOUNT HOLDER NAME: {name}",fg='white',font=('orbitron',15))
                empty_label.pack(fill="x",pady=5)

                amount_label = tk.Label(self,text="WITHDRAW AMOUNT:",bg='#9933ff',fg='white',font=('orbitron',15))
                amount_label.pack(pady=10,anchor='w',padx=30)

                amount_entry = tk.Entry(self,width=50)
                amount_entry.focus()
                amount_entry.pack(ipadx=15,pady=10,ipady=5)

                withdraw = tk.PhotoImage(file=r"C:\project\withdraw.png")
                withdraw_photo = withdraw.subsample(20,20)

                add_button = tk.Button(self,text="  WITHDRAW",bg='#330066',fg='white',font=('orbitron',15),width=15,command=sub,bd=5,
                                       image=withdraw_photo,compound=tk.LEFT)
                add_button.image = withdraw_photo
                add_button.pack(ipadx=140,pady=10,ipady=3)
                
                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(MainPage),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=95,pady=10,ipady=3)

                info_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15),width=25)
                info_label.pack(pady=10)


class TransactionPage(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'
                name = master.data()[0]

                def Tran():
                        data = master.data()
                        sender_acnum = data[4]
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Amount FROM UserData WHERE AcNum = {sender_acnum}")
                                sender_balance = cursor.fetchall()
                        sender_balance = sender_balance[0][0]
                        
                        if amount_entry.get() == "":
                                warning_label['text'] = "ENTER THE AMOUNT"
                                return
                        elif int(amount_entry.get()) <= 0:
                                warning_label['text'] = "ENTER POSITIVE NUMBER"
                                return
                        elif sender_balance >= int(amount_entry.get()):
                                amount_in = int(amount_entry.get())
                        else:
                                warning_label['text'] = "DO DON'T HAVE \nENOUGH MONEY TO SEND"
                                return
                        try:
                                ac_num = int(acnum_entry.get())
                                with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                        cursor = connection.cursor()
                                        cursor.execute(f"SELECT Amount FROM UserData WHERE AcNum = {ac_num}")
                                        cash = cursor.fetchall()
                                if cash == []:
                                        warning_label['text'] = "INVALID ACCOUNT NUMBER"
                                else:
                                        cash = cash[0][0]
                                        up_send = sender_balance - amount_in
                                        if ac_num == sender_acnum:
                                                warning_label['text'] = "YOU CANNOT SEND \nMONEY TO YOURSELF"
                                                up_re = up_send + amount_in
                                        else:
                                                up_re = cash + amount_in
                                        cash_up = [up_send,up_re]
                                        acc_num = [sender_acnum,ac_num]
                                        for i in range(0,2):
                                                with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                                        cursor = connection.cursor()
                                                        cursor.execute(f"UPDATE UserData SET Amount = {cash_up[i]} WHERE AcNum = {acc_num[i]};")
                                                        warning_label['text'] = "MONET SEND SUCCESSFULLY"
                                                        
                                                
                        except ValueError:
                                warning_label['text'] = "INVALID ACCOUNT NUMBER"
                                        
                        
                
                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)
                
                empty_label = tk.Label(self,bg='#9933ff',height=2,text=f"ACCOUNT HOLDER NAME: {name}",fg='white',font=('orbitron',15))
                empty_label.pack(fill="x",pady=5)

                acnum_label = tk.Label(self,text="RECEIVER ACCOUNT NUMBER: ",bg='#9933ff',fg='white',font=('orbitron',15))
                acnum_label.pack(pady=10)

                acnum_entry = tk.Entry(self)
                acnum_entry.focus()
                acnum_entry.pack(ipady=3,fill='x',padx=25,pady=5)

                amount_label = tk.Label(self, text="AMOUNT TO SEND: ",bg='#9933ff',fg='white',font=('orbitron',15))
                amount_label.pack(pady=10,anchor='w',ipadx=25)

                amount_entry = tk.Entry(self)
                amount_entry.pack(ipady=3,fill='x',padx=25,pady=5)

                tran = tk.PhotoImage(file=r"C:\project\transaction1.png")
                tran_photo = tran.subsample(20,20)

                send_button = tk.Button(self,text="  SEND",font=('orbitron',15),bg="#330066",fg="white",width=15,bd=5,command=Tran,
                                        image=tran_photo,compound=tk.LEFT)
                send_button.image = tran_photo
                send_button.pack(ipadx=150,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(MainPage),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                warning_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15))
                warning_label.pack(pady=10)

class AccountCreation(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'
                c = None
                def Create():
                        a = False
                        b = False
                        c = False
                        if check.get() == "":
                                warning_label['text'] = "YOU MUST AGREE THE \n TERMS AND CONDITIONS"
                        elif check.get() == 0:
                                warning_label['text'] = "YOU MUST AGREE THE \n TERMS AND CONDITIONS"
                        else:
                                c = True
                                
                        if name_entry.get() == "":
                                warning_label['text'] = "ENTER YOUR NAME"
                        for i in name_entry.get():
                                if i.isdigit():
                                        warning_label['text'] = "DONOT USE NUMBERS \n IN NAME"
                                        break
                                else:
                                        a = True
                                        
                        if amount_entry.get() == "":
                                warning_label['text'] = "ENTER INTIAL AMOUNT"
                        elif int(amount_entry.get()) >= 500:
                                b = True
                        elif int(amount_entry.get()) <= 500:
                                warning_label['text'] = "INTIAL AMOUNT MUST \n  500 OR ABOVE"
                        else:
                                warning_label['text'] = "ENTER VALID AMOUNT"
                                
                        if email_entry.get() == "":
                                warning_label['text'] = "ENTER YOUR EMAIL"

                                
                        if a and b and c :
                                data = [name_entry.get(),int(amount_entry.get()),email_entry.get()]
                                master.new_data(data)
                                master.switch_frame(OTP_Page)


                        
                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2)
                empty_label.pack()

                name_label = tk.Label(self,text="      NAME: ",bg='#9933ff',fg='white',font=('orbitron',15))
                name_label.pack(anchor='w',pady=5)

                name_entry = tk.Entry(self)
                name_entry.focus()
                name_entry.pack(pady=5,ipady=5,ipadx=100)

                amount_label = tk.Label(self,text="      INITIAL AMOUNT: ",bg='#9933ff',fg='white',font=('orbitron',15))
                amount_label.pack(anchor='w',pady=5)

                amount_entry = tk.Entry(self)
                amount_entry.pack(pady=5,ipady=5,ipadx=100)

                email_label = tk.Label(self,text="      E-MAIL: ",bg='#9933ff',fg='white',font=('orbitron',15))
                email_label.pack(anchor='w',pady=5)

                email_entry = tk.Entry(self)
                email_entry.pack(pady=5,ipady=5,ipadx=100)

                check = tk.StringVar()

                ttk.Checkbutton(self,text="I AGREE THE TERMS AND CONDITIONS",variable=check).pack(pady=10)

                create = tk.PhotoImage(file=r"C:\project\upload.png")
                create_photo = create.subsample(20,20)

                create_button = tk.Button(self,text="  CREATE",bg="#330066",fg='white',font=('orbitron',15),bd=5,command=Create,image=create_photo,compound=tk.LEFT)
                create_button.image = create_photo
                create_button.pack(ipadx=95,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(SignIn),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                warning_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15),width=20)
                warning_label.pack(pady=5)

class DeleteAccount(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')                     
                self.master = master
                self.master['bg'] = '#9933ff'

                def delete_ac():
                        if account_entry.get() == "":
                                warning_label['text'] = 'ENTER THE ACCOUNT \nNUMBER'
                                return
                        Ac_num = int(account_entry.get())
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Password FROM UserData WHERE AcNum = {Ac_num}")
                                password = cursor.fetchall()
                        if password == []:
                                warning_label['text'] = "INVALID ACCOUNT NUMBER"
                        elif password_entry.get() == "":
                                warning_label['text'] = "ENTER YOUR PASSWORD"
                        elif password_entry.get() == password[0][0]:
                                with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                        cursor = connection.cursor()
                                        cursor.execute(f"DELETE FROM UserData WHERE AcNum = {Ac_num};")
                                        warning_label['text'] = "ACCOUNT DELETED \nSUCCESSFULLY"
                        else:
                                warning_label['text'] = "INCORRECT PASSWORD"

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2)
                empty_label.pack()

                account_num = tk.Label(self,text="ACCOUNT NUMBER:",bg='#9933ff',fg='white',font=('orbitron',15))
                account_num.pack(anchor='w',padx=40,pady=5)
                
                account_entry = tk.Entry(self)
                account_entry.focus()
                account_entry.pack(pady=5,ipady=5,ipadx=100)

                password_label = tk.Label(self,text="PASSWORD:",bg='#9933ff',fg='white',font=('orbitron',15))
                password_label.pack(anchor='w',padx=40,pady=5)

                password_entry = tk.Entry(self)
                password_entry.pack(pady=5,ipady=5,ipadx=100)

                del1 = tk.PhotoImage(file=r"C:\project\delete.png")
                del2 = del1.subsample(20,20)

                delete_button = tk.Button(self,text="  DELETE",bg="#330066",fg='white',font=('orbitron',15),bd=5,width=15,command=delete_ac,
                                          image=del2,compound=tk.LEFT)
                delete_button.image = del2
                delete_button.pack(ipadx=145,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(SignIn),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)


                warning_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15))
                warning_label.pack(pady=5)

class OTP_Page(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'

                datas = master.send()
                email = datas[2]
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                ''' remove Account_name and password than write your google account name and password there '''
                s.login("Account_name", "password")
                ac_num = random.randint(100000,999999)
                message = f"""\
Subject:THANK FOR USING


YOUR OTP IS {ac_num}..."""
                #only google account name
                s.sendmail("Account_name",email, message)
                s.quit()

                

                def check():
                        if ac_num == int(OTP_entry.get()):
                                master.switch_frame(AccountCreationFinal)
                                

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                label = tk.Label(self,text="OTP VERIFICATION",bg='#9933ff',fg='white',font=('orbitron',20))
                label.pack(pady=20)

                OTP_entry = tk.Entry(self)
                OTP_entry.focus()
                OTP_entry.pack(pady=10,ipadx=80,ipady=5)

                con1 = tk.PhotoImage(file=r"C:\project\checkmark.png")
                con2 = con1.subsample(20,20)

                confirm_button = tk.Button(self,text="  CONFIRM",font=('orbitron',15),bg="#330066",fg="white",width=15,bd=5,command=check,
                                           image=con2,compound=tk.LEFT)
                confirm_button.image = con2
                confirm_button.pack(ipadx=145,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(AccountCreation),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                quit1 = tk.PhotoImage(file=r"C:\project\power.png")
                quit2 = quit1.subsample(20,20)
                
                quit_button = tk.Button(self,text="  QUIT",font=('orbitron',15),bg="#330066",fg="white",width=5,command=lambda:master.switch_frame(SignIn),bd=5,
                                        image=quit2,compound=tk.LEFT)
                quit_button.image = quit2
                quit_button.pack(ipadx=150,pady=15,ipady=3)

                
class AccountCreationFinal(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')                     
                self.master = master
                self.master['bg'] = '#9933ff'

                def set_up():
                        pass
                        datas = master.send()
                        name = datas[0]
                        amount = datas[1]
                        email = datas[2]
                        if len(password_entry.get()) < 4:
                                warning_label['text'] = "YOUR PASSWORD MUST \nHAVE 4 OR MORE CHARACTERS"
                        elif password_entry.get() != confirm_entry.get():
                                 warning_label['text'] = "PASSWORD DOESNOT MATCH"
                        else:
                                pasw = True
                                pass_w = password_entry.get()
                        if pasw:
                                with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                        cursor = connection.cursor()
                                        cursor.execute(
                                                f"INSERT INTO UserData Values('{name}',{amount},'{email}','{pass_w}',{account_number});"
                                                )
                                        showinfo(title='Information',message='ACCOUNT CREATED SUCCESSFULLY')
                                        master.switch_frame(SignIn)
                        

                def show():
                        if int(check.get()) == 0:
                                password_entry['show'] = "X"
                                confirm_entry['show'] = "X"
                        else:
                                password_entry['show'] = ""
                                confirm_entry['show'] = ""

                account_number = random.randint(10000000,99999999)

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                ac_label = tk.Label(self,text=f"YOUR ACCOUNT NUMBER IS\n{account_number}",bg='#9933ff',fg='white',font=('orbitron',20))
                ac_label.pack(pady=10)

                password_label = tk.Label(self,text="   CREATE PASSWORD:",bg='#9933ff',fg='white',font=('orbitron',15))
                password_label.pack(pady=10,anchor='w')

                password_entry = tk.Entry(self,show="X")
                password_entry.focus()
                password_entry.pack(pady=5,ipady=5,ipadx=130)

                confirm_label = tk.Label(self,text="   CONFIRM PASSWORD:",bg='#9933ff',fg='white',font=('orbitron',15))
                confirm_label.pack(pady=10,anchor='w')

                confirm_entry = tk.Entry(self,show="X")
                confirm_entry.pack(pady=5,ipady=5,ipadx=130)

                check = tk.StringVar()

                ttk.Checkbutton(self,text="SHOW PASSWORD",variable=check,command=show).pack(pady=10)

                finish = tk.PhotoImage(file=r"C:\project\check.png")
                finish1 = finish.subsample(20,20)

                finish_button = tk.Button(self,text="  FINISH",font=('orbitron',15),bg="#330066",fg="white",width=15,bd=5,command=set_up,image=finish1,compound=tk.LEFT)
                finish_button.image = finish1
                finish_button.pack(ipadx=150,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(AccountCreation),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                warning_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15))
                warning_label.pack(pady=10)

class ChangePassword(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')                     
                self.master = master
                self.master['bg'] = '#9933ff'

                def send():
                        try:
                                acnum = int(account_entry.get())
                        except ValueError:
                                warning_label['text'] = "INVALID ACCOUNT NUMBER"
                                return None
                        with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                cursor = connection.cursor()
                                cursor.execute(f"SELECT Email FROM UserData WHERE AcNum = {acnum};")
                                email = cursor.fetchall()[0][0]
                                master.new_data([acnum,email])
                                master.switch_frame(OTP_FOR_PASS)

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2,text="CHANGE PASSWORD",fg='white',font=('orbitron',20))
                empty_label.pack(pady=10)

                account_num = tk.Label(self,text="ACCOUNT NUMBER:",bg='#9933ff',fg='white',font=('orbitron',15))
                account_num.pack(anchor='w',padx=40,pady=5)
                
                account_entry = tk.Entry(self)
                account_entry.focus()
                account_entry.pack(pady=5,ipady=5,ipadx=100)
                
                otp = tk.PhotoImage(file=r"C:\project\OTP.png")
                otp1 = otp.subsample(20,20)

                finish_button = tk.Button(self,text="  GET OTP",font=('orbitron',15),bg="#330066",fg="white",width=15,bd=5,command=send,image=otp1,compound=tk.LEFT)
                finish_button.image = otp1
                finish_button.pack(ipadx=145,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(SignIn),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                warning_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15))
                warning_label.pack(pady=10)

class OTP_FOR_PASS(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'

                email = master.send()[1]
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                ''' remove Account_name and password than write your google account name and password there '''
                s.login("Account_name", "Password")
                ac_num = random.randint(100000,999999)
                message = f"""\
Subject:THANK FOR USING


YOUR OTP IS {ac_num}..."""
                #only google account name
                s.sendmail("Account_name",email, message)
                s.quit()

                

                def check():
                        if ac_num == int(OTP_entry.get()):
                                master.switch_frame(NewPassword)
                                

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                label = tk.Label(self,text="OTP VERIFICATION",bg='#9933ff',fg='white',font=('orbitron',20))
                label.pack(pady=20)

                OTP_entry = tk.Entry(self)
                OTP_entry.focus()
                OTP_entry.pack(pady=10,ipadx=80,ipady=5)

                con = tk.PhotoImage(file=r"C:\project\checkmark.png")
                con1 = con.subsample(20,20)

                confirm_button = tk.Button(self,text="CONFIRM",font=('orbitron',15),bg="#330066",fg="white",width=15,bd=5,command=check,image=con1,compound=tk.LEFT)
                confirm_button.image = con1
                confirm_button.pack(ipadx=145,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"F:\subtitles\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(ChangePassword),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                quit1 = tk.PhotoImage(file=r"C:\project\power.png")
                quit2 = quit1.subsample(20,20)
                
                quit_button = tk.Button(self,text="  QUIT",font=('orbitron',15),bg="#330066",fg="white",width=5,command=lambda:master.switch_frame(SignIn),bd=5,
                                        image=quit2,compound=tk.LEFT)
                quit_button.image = quit2
                quit_button.pack(ipadx=150,pady=15,ipady=3)

class NewPassword(tk.Frame):
        def __init__(self,master):
                tk.Frame.__init__(self,master,bg='#9933ff')
                self.master = master
                self.master['bg'] = '#9933ff'

                acnum = master.send()[0]

                def show():
                        if int(check.get()) == 0:
                                password_entry['show'] = "X"
                                confirm_entry['show'] = "X"
                        else:
                                password_entry['show'] = ""
                                confirm_entry['show'] = ""
                def setpassword():
                        if password_entry.get() == "":
                                warning_label['text'] = "SET NEW PASSWORD"
                                return
                        elif password_entry.get() != confirm_entry.get():
                                warning_label['text'] = "PASSWORD DOESNOT MATCH"
                                return
                        elif len(password_entry.get()) < 4:
                                warning_label['text'] = "PASSWORD MUST HAVE \n4 OR MORE CHARACTERS"
                                return
                        else:
                                password = password_entry.get()
                                with sqlite3.connect("ATM_DATABASE1.db") as connection:
                                        cursor = connection.cursor()
                                        cursor.execute(f"UPDATE UserData SET Password = '{password}' WHERE AcNum = {acnum};")
                                        showinfo(title='Information',message='PASSWORD CHANGED SUCCESSFULLY')
                                        master.switch_frame(SignIn)
                                

                heading_label = tk.Label(self,text="INDIAN BANK ATM",bg='#9933ff',fg='white',font=('orbitron',30))
                heading_label.pack(pady=10)

                empty_label = tk.Label(self,bg='#9933ff',height=2)
                empty_label.pack()

                password_label = tk.Label(self,text="   CREATE PASSWORD:",bg='#9933ff',fg='white',font=('orbitron',15))
                password_label.pack(pady=10,anchor='w')

                password_entry = tk.Entry(self,show="X")
                password_entry.focus()
                password_entry.pack(pady=5,ipady=5,ipadx=130)

                confirm_label = tk.Label(self,text="   CONFIRM PASSWORD:",bg='#9933ff',fg='white',font=('orbitron',15))
                confirm_label.pack(pady=10,anchor='w')

                confirm_entry = tk.Entry(self,show="X")
                confirm_entry.pack(pady=5,ipady=5,ipadx=130)

                check = tk.StringVar()

                ttk.Checkbutton(self,text="SHOW PASSWORD",variable=check,command=show).pack(pady=10)

                finish = tk.PhotoImage(file=r"C:\project\check.png")
                finish1 = finish.subsample(20,20)

                finish_button = tk.Button(self,text="  FINISH",font=('orbitron',15),bg="#330066",fg="white",width=15,bd=5,command=setpassword,image=finish1,compound=tk.LEFT)
                finish_button.image = finish1
                finish_button.pack(ipadx=150,pady=10,ipady=3)

                back = tk.PhotoImage(file=r"C:\project\back.png")
                back_photo = back.subsample(20,20)

                back_button = tk.Button(self,text="  BACK",font=('orbitron',15),bg="#330066",fg="white",command=lambda:master.switch_frame(ChangePassword),bd=5,
                                        image=back_photo,compound=tk.LEFT)
                back_button.image = back_photo
                back_button.pack(ipadx=100,pady=10,ipady=3)

                warning_label = tk.Label(self,text="",bg='#9933ff',fg='white',font=('orbitron',15))
                warning_label.pack(pady=10)
        
app = atm()
app.mainloop()
