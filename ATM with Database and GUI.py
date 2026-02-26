import random
import csv
import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("MABUHAY BANK SYSTEM")
bank_accounts = []
database_file = "mabuhay_database.csv"

class BankAccount:
    def __init__(self, name, acc_number, pin, balance, debt):
        self.name = name
        self.acc_number = acc_number
        self.pin = pin
        self.balance = balance
        self.debt = debt

def upd_db():
    try:
        with open(database_file, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Name", "Account Number", "PIN", "Balance", "Debt"])
            for acc in bank_accounts:
                csv_writer.writerow([acc.name, acc.acc_number, acc.pin, acc.balance, acc.debt])
        print("Data successfully saved!")
    except PermissionError:
        messagebox.showerror("Error", "Close database file and try again.")
        return

def load_db():
    if os.path.isfile(database_file):
        try:
            with open(database_file, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader, None)
                for row in csv_reader:
                    if row:
                        load_accs = BankAccount(row[0], int(row[1]), int(row[2]), float(row[3]), float(row[4]))
                        bank_accounts.append(load_accs)
                print(f"Successfully loaded {len(bank_accounts)} account!")
        except FileNotFoundError:
            print("ERROR! File doesn't exist!")

def clear():
    for widget in root.winfo_children():
        widget.destroy()
    root.unbind('<Return>')

def bank_main():
    clear()
    root.geometry("1000x500")
    root.resizable(False, False)
    kaliwa = Frame(root, bg='black')
    kaliwa.pack(side='left', fill='both')
    Label(kaliwa, text="MABUHAY BANK", font=("Arial Bold", 50),
          bg='black', fg='white').pack(anchor='w', padx=50, pady=(180, 0))
    Label(kaliwa, text="Where banking meets comfort", font=("Arial Bold", 15),
          bg='black', fg='white').pack(anchor='w', padx=55, pady=0)

    kanan = Frame(root)
    kanan.pack(side='right', fill='both')
    Button(kanan, text="Create Account", command=name_create, activebackground='black',
           activeforeground='white', bg='black', fg='white', pady=10, width=30).pack(pady=(177,0), padx=(0, 65))
    Button(kanan, text="Login", command=login, activebackground='black',
           activeforeground='white', bg='black', fg='white', pady=10, width=30).pack(padx=(0, 65), pady=(2,0))
    Button(kanan, text="Exit", command=root.quit, activebackground='black',
           activeforeground='white', bg='black', fg='white', pady=10, width=30).pack(padx=(0, 65), pady=2)

def name_create():
    def next1():
        first = firstname.get()
        if not first:
            messagebox.showerror("Error", "First name is required")
            return
        first = first.capitalize()
        last = lastname.get()
        if not last:
            messagebox.showerror("Error", "Last name is required")
            return
        last = last.capitalize()
        name = f"{first} {last}"
        if name.replace(" ", "").isalpha():
            pin_create(name)
        else:
            messagebox.showerror("Error", "Name must contain only letters.")
            firstname.focus()

    clear()
    root.geometry("600x400")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=50)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 10),
          bg='black', fg='white').pack(side='right', padx=(35,10 ), pady=20)
    Label(root, text="Create an Account", font=("arial bold", 20), pady=20).pack(pady=(50,2))
    Label(root, text="First name:", font=("Arial", 10)).pack(anchor='w', padx=(160,0))
    firstname = Entry(root, width=30, font=('Arial', 12))
    firstname.pack()

    Label(root, text="Last name:", font=("Arial", 10)).pack(anchor='w', padx=(160,0))
    lastname = Entry(root, width=30, font=('arial', 12))
    lastname.pack()

    firstname.focus()
    Button(root,text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=bank_main).pack(side='right', pady=(90,5),padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=next1).pack(side='right', pady=(90, 5), padx=1)

def pin_create(name):
    def next2():
        if len(pinn.get()) == 4 and pinn.get().isdigit():
            pin = int(pinn.get())
            bal_inp(pin, name)
        else:
            messagebox.showerror("Error", "PIN must be 4 digits.")
            pinn.focus()

    clear()
    root.geometry("400x250")
    root.resizable(False, False)
    Label(root, text="Account Registration", font=("arial bold", 20), pady=20).pack(pady=(35,2),padx=(15,0))
    Label(root, text="Enter 4-digit PIN:", font=("Arial", 10)).pack(anchor='w', padx=(85,0))
    pinn = Entry(root, width=25, show="*", font=('Arial', 12))
    pinn.required = True
    pinn.pack(anchor='w', padx=(85,0))
    pinn.focus()
    Button(root, text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=name_create).pack(side='right', pady=(60, 0), padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=next2).pack(side='right', pady=(60, 0), padx=1)

def bal_inp(pin, name):
    def next3():
        try:
            bal = bal_in.get()
            balance = float(bal.replace(',', ''))
            if balance >= 20000:
                while True:
                    acc_number = random.randint(1000000, 9999999)
                    if not any(acc.acc_number == acc_number for acc in bank_accounts):
                        break
                verify(acc_number, pin, name, balance, 0)
            else:
                messagebox.showerror("Error", "Invalid input.")
                bal_in.focus()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")
            bal_in.focus()

    clear()
    root.geometry("500x300")
    root.resizable(False, False)
    Label(root, text="Account Registration", font=("arial bold", 20), pady=20).pack(pady=(50,10))
    Label(root, text="Your account balance is ZERO. \nEnter atleast ₱20,000 initial deposit:",
          font=("Arial", 10), justify='left').pack(anchor='w',padx=(112,5))
    bal_in = Entry(root, width=30, font=("arial",12))
    bal_in.pack()
    bal_in.focus()
    Button(root, text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=name_create).pack(side='right', pady=(68, 0), padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=next3).pack(side='right', pady=(68, 0), padx=1)

def verify(acc_number, pin, name, balance, debt):
    def yey():
        new_bank = BankAccount(name, acc_number, pin, balance, debt)
        bank_accounts.append(new_bank)
        upd_db()
        messagebox.showinfo(f"WELCOME, {name.upper()}!", f"""
Your account has been successfully created.
Your account number is {acc_number}.
Your balance is {balance}.""")
        clear()
        bank_main()

    clear()
    root.resizable(False, False)
    Label(root, text="Confirm account registration?").pack()
    Button(root, text="Confirm", bg='black', fg='white', activebackground='black', activeforeground='white',
           command=yey, pady=10, width=30).pack()
    Button(root, text="Cancel", bg='black', fg='white', activebackground='black', activeforeground='white',
           command=name_create, pady=10, width=30).pack()

def login():
    def validate():
        ipin = user_pin.get()
        numu = user_num.get()
        found_acc = None
        for acc in bank_accounts:
            if numu == str(acc.acc_number):
                found_acc = acc
                break
        if found_acc:
            if len(ipin) == 4 and ipin.isdigit():
                pin = int(ipin)
                if pin == found_acc.pin:
                    messagebox.showinfo(f"WELCOME, {found_acc.name.upper()}", "Login successful.")
                    atm(found_acc)
                else:
                    messagebox.showerror("Error", "Incorrect PIN.")
                    user_pin.focus()
            else:
                messagebox.showerror("Error", "Invalid PIN input.")
                user_pin.focus()
        else:
            messagebox.showerror("Error", "Account number not found.")
            user_num.focus()

    clear()
    root.geometry("600x400")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=50)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 10),
          bg='black', fg='white').pack(side='right', padx=(35,10 ), pady=20)
    Label(root, text="Login", font=("arial bold", 20), pady=20).pack(pady=(50,2))
    Label(root, text="Account Number:", font=("Arial", 10)).pack(anchor='w', padx=(160,0))
    user_num = Entry(root, width=30, font=('Arial', 12))
    user_num.pack()

    Label(root, text="4-digit PIN:", font=("Arial", 10)).pack(anchor='w', padx=(160,0))
    user_pin = Entry(root, width=30, font=('arial', 12), show="*")
    user_pin.pack()

    user_num.focus()
    Button(root,text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=bank_main).pack(side='right', pady=(90,5),padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=validate).pack(side='right', pady=(90, 5), padx=1)

def deposit(found_acc):
    clear()
    def cont():
        depp = depamount.get()
        depp = depp.replace(',', '')
        if depp.isdigit():
            depp = int(depp)
            if 5000 <= depp <= 100000:
                found_acc.balance = found_acc.balance + depp
                upd_db()
                messagebox.showinfo("Success", f"Deposit successful. New balance is {found_acc.balance}.")
                atm(found_acc)
            else:
                messagebox.showerror("Error", "Invalid deposit input.")
                depamount.focus()
        else:
            messagebox.showerror("Error", "Invalid deposit input.")
            depamount.focus()

    root.geometry("600x400")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=50)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 10),
          bg='black', fg='white').pack(side='right', padx=(35,10 ), pady=20)

    Label(root, text="Deposit", font=("verdana bold", 20), pady=20).pack(pady=(50,2))
    Label(root, text="Enter amount (Min. ₱5,000, Max. 100,000):", font=("Verdana", 10)).pack(anchor='w', padx=(160,0))
    depamount = Entry(root, width=30, font=('Verdana', 12))
    depamount.pack()

    depamount.focus()
    Button(root,text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=lambda: atm(found_acc)).pack(side='right', pady=(90,5),padx=1)
    Button(root, text="Next", width=10,bg='black', fg='white', activebackground='black', activeforeground='white',
           command=cont).pack(side='right', pady=(90, 5), padx=1)

def withdraw(found_acc):
    clear()
    def cont2():
        am = ww.get()
        am = am.replace(",", "")
        if am.isdigit():
            amount_withdraw = int(am)
            if found_acc.balance < amount_withdraw:
                messagebox.showerror("Error!", "Insufficient balance.")
            else:
                if 1000 <= amount_withdraw <= 50000:
                    found_acc.balance = found_acc.balance - amount_withdraw
                    upd_db()
                    messagebox.showinfo("Success", f"""Withdrawal successful.
New balance is {found_acc.balance}.""")
                    atm(found_acc)
                else:
                    messagebox.showerror("Error", "Invalid withdrawal input.")
                    ww.focus()
        else:
            messagebox.showerror("Error", "Invalid withdrawal input.")
            ww.focus()

    root.geometry("600x400")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=50)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 10),
          bg='black', fg='white').pack(side='right', padx=(35,10 ), pady=20)

    Label(root, text="Withdraw", font=("Verdana bold", 20), pady=20).pack(pady=(50,2))
    Label(root, text="Enter amount (Min. ₱1,000, Max. ₱50,000):", font=("verdana", 10)).pack(anchor='w', padx=(160,0))
    ww = Entry(root, width=30, font=('verdana', 12))
    ww.pack()

    ww.focus()
    Button(root,text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=lambda: atm(found_acc)).pack(side='right', pady=(90,5),padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=cont2).pack(side='right', pady=(90, 5), padx=1)

def loan(found_acc):
    def check():
        hm = choose.get()
        mnths = choose2.get()
        if found_acc.debt > 0:
            messagebox.showerror("Error", f"Please settle outstanding debt: ₱{found_acc.debt}")
            atm(found_acc)
        elif hm == "Choose an option":
            messagebox.showerror("Error", "Select a valid option.")
            return
        elif mnths == "Choose an option":
            messagebox.showerror("Error", "Select a valid option.")
            return
        elif int(hm.replace(',','').replace('₱','')) == 5000:
            if mnths == "3 months to pay (5% interest)":
                found_acc.balance = found_acc.balance + 5000
                found_acc.debt = found_acc.debt + 5000 + (5000 * 0.05)
                upd_db()
                messagebox.showinfo("Success", f"""Loan successful.
New balance is {found_acc.balance}. Debt is {found_acc.debt}.""")
                atm(found_acc)
            elif mnths == "6 months to pay (8% interest)":
                found_acc.balance = found_acc.balance + 5000
                found_acc.debt = found_acc.debt + 5000 + (5000 * 0.08)
                upd_db()
                messagebox.showinfo("Success", f"""Loan successful.
New balance is {found_acc.balance}. Debt is {found_acc.debt}.""")
                atm(found_acc)
        elif int(hm.replace(',', '').replace('₱', '')) == 10000:
            if mnths == "3 months to pay (5% interest)":
                found_acc.balance = found_acc.balance + 10000
                found_acc.debt = found_acc.debt + 10000 + (10000 * 0.05)
                upd_db()
                messagebox.showinfo("Success", f"""Loan successful.
New balance is {found_acc.balance}. Debt is {found_acc.debt}.""")
                atm(found_acc)
            elif mnths == "6 months to pay (8% interest)":
                found_acc.balance = found_acc.balance + 10000
                found_acc.debt = found_acc.debt + 10000 + (10000 * 0.08)
                upd_db()
                messagebox.showinfo("Success", f"""Loan successful.
New balance is {found_acc.balance}. Debt is {found_acc.debt}.""")
                atm(found_acc)

    clear()
    root.geometry("600x400")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=50)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 10),
          bg='black', fg='white').pack(side='right', padx=(35, 10), pady=20)
    Label(root, text="Loan Application", font=("Verdana bold", 20), pady=20).pack(pady=(50,2))

    frame_nanaman = Frame(root)
    frame_nanaman.pack(pady=10)
    Label(frame_nanaman, text="Select amount",
          font=("verdana", 10)).grid(row=0, column=0, pady=(0,5), padx=(0,4), sticky='w')
    Label(frame_nanaman, text="Select due",
          font=("verdana", 10)).grid(row=0, column=1, sticky='w', padx=(0,4), pady=(0,5))

    choice = ["₱5,000", "₱10,000"]
    choice2 = ["3 months to pay (5% interest)", "6 months to pay (8% interest)"]

    choose = ttk.Combobox(frame_nanaman, values=choice, state='readonly', font=("Verdana", 10))
    choose.set("Choose an option")
    choose.grid(row=1, column=0, padx=(0,20), pady=(0,20), sticky='w')

    choose2 = ttk.Combobox(frame_nanaman, values=choice2, state='readonly', font=("Verdana", 10))
    choose2.set("Choose an option")
    choose2.grid(row=1, column=1, pady=(0,20), sticky='w')

    choose.focus()
    frame_pa = Frame(root)
    frame_pa.pack(side='bottom',fill='x')
    Button(root,text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=lambda: atm(found_acc)).pack(side='right', pady=(90,0),padx=1)
    yo = Button(root, text="Next", width=10,bg='black', fg='white', activebackground='black', activeforeground='white',
           command=check, state='disabled')
    yo.pack(side='right', pady=(90, 0), padx=1)

    wow = tkinter.IntVar()
    sure = Checkbutton(frame_nanaman, text="""Failure to settle payment will result in the
automatic deduction to my balance.""", font=("Verdana", 10), variable=wow,
    command=lambda: yo.configure(state='normal' if wow.get() else 'disabled'))
    sure.grid(row=2, column=0, padx=(0, 20), pady=(0, 20), columnspan=3)

def change_name(found_acc):
    clear()
    root.geometry("600x400")
    root.resizable(False, False)
    def check2():
        first = firstname.get()
        first = first.capitalize()
        last = lastname.get()
        last = last.capitalize()
        name = f"{first} {last}"
        if name.replace(" ", "").isalpha():
            found_acc.name = name
            upd_db()
            messagebox.showinfo("Change name Successful", f"Mabuhay, {found_acc.name}!")
            sett(found_acc)
        else:
            messagebox.showerror("Error", "Name must contain only letters.")
            firstname.focus()

    header = Frame(root, bg='black', height=50)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 10),
          bg='black', fg='white').pack(side='right', padx=(35, 10), pady=20)

    Label(root, text="Change Name", font=("arial bold", 20), pady=20).pack(pady=(50, 2))
    Label(root, text="First name:", font=("Arial", 10)).pack(anchor='w', padx=(160, 0))
    firstname = Entry(root, width=30, font=('Arial', 12))
    firstname.pack()

    Label(root, text="Last name:", font=("Arial", 10)).pack(anchor='w', padx=(160, 0))
    lastname = Entry(root, width=30, font=('arial', 12))
    lastname.pack()

    firstname.focus()
    Button(root, text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=lambda: sett(found_acc)).pack(side='right', pady=(90, 5), padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=check2).pack(side='right', pady=(90, 5), padx=1)

def change_pin(found_acc):
    def hays():
        if len(change.get()) == 4 and change.get().isdigit():
            pin = int(change.get())
            found_acc.pin = pin
            upd_db()
            messagebox.showinfo("Success!", "Change PIN Successful.")
        else:
            messagebox.showerror("Error", "PIN must be 4 digits.")
            change.focus()

    clear()
    root.geometry("400x250")
    root.resizable(False, False)
    Label(root, text="Change PIN", font=("arial bold", 20), pady=20).pack(pady=(35, 2), padx=(15, 0))
    Label(root, text="Enter 4-digit PIN:", font=("Arial", 10)).pack(anchor='w', padx=(85, 0))
    change = Entry(root, width=25, show="*", font=('Arial', 12))
    change.pack(anchor='w', padx=(85, 0))
    change.focus()
    Button(root, text="Cancel", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=lambda: sett(found_acc)).pack(side='right', pady=(60, 0), padx=1)
    Button(root, text="Next", width=10, bg='black', fg='white', activebackground='black', activeforeground='white',
           command=hays).pack(side='right', pady=(60, 0), padx=1)

def delete(found_acc):
    if found_acc.debt > 0:
        messagebox.showerror("Error", f"Settle outstanding debt of ₱{found_acc.debt}")
        return
    else:
        yahoo = messagebox.askyesno("Warning!", "Are you sure you want to delete this account?")
        if yahoo:
            if found_acc in bank_accounts:
                bank_accounts.remove(found_acc)
                upd_db()
                messagebox.showinfo("Sad to see you go :(", "Account successfully deleted.")
                bank_main()
        else:
            return

def sett(found_acc):
    clear()
    root.geometry("800x550")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=80)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 15),
          bg='black', fg='white').pack(side='right', padx=30, pady=20)

    ewan = Frame(root)
    ewan.pack(expand=True, fill='both')
    Label(ewan, text=f"Account Settings",
          font=("Verdana bold", 30)).pack(side='top',anchor='w', pady=(40,0), padx=(10,0))
    Label(ewan, text=f"Account number: {found_acc.acc_number}",
          font=("Verdana bold", 15)).pack(side='top',anchor='w', pady=(0,0), padx=(10,0))

    butones = Frame(ewan)
    butones.pack(anchor='w', padx=20, pady=(115, 0))
    Button(butones, text="Change Name", font=('verdana', 15), bg='black', command=lambda: change_name(found_acc),
           fg='white', width=17, height=1, activebackground='black').grid(row=3,column=0, padx=(15,0), pady=(0,20))
    Button(butones, text="Change PIN", font=('verdana', 15), bg='black', command=lambda: change_pin(found_acc),
           fg='white', width=17, height=1, activebackground='black').grid(row=3, column=1, padx=(20,0), pady=(0,20))
    Button(butones, text="Delete Account", font=('verdana', 15), bg='black', command=lambda: delete(found_acc),
           fg='white', width=17, height=1, activebackground='black').grid(row=3, column=2, padx=(20,0), pady=(0,20))
    Button(butones, text="Exit", font=('verdana', 15), bg='black', fg='white', width=17, height=1,
           command=lambda: atm(found_acc), activebackground='black').grid(row=4, column=1, padx=(20,0), pady=(0,25))

def atm(found_acc):
    clear()
    root.geometry("800x550")
    root.resizable(False, False)
    header = Frame(root, bg='black', height=80)
    header.pack(side='top', fill='x')
    Label(header, text="MABUHAY BANK", font=("Verdana bold", 15),
          bg='black', fg='white').pack(side='right', padx=30, pady=20)

    ewan = Frame(root)
    ewan.pack(expand=True, fill='both')
    Label(ewan, text=f"Mabuhay, {found_acc.name}!",
          font=("Verdana bold", 25)).pack(side='top',anchor='w', pady=(40,0), padx=(10,0))
    Label(ewan, text=f"{found_acc.balance} balance.",
          font=("Verdana bold", 15)).pack(side='top',anchor='w', pady=(0,0), padx=(10,0))

    butones = Frame(ewan)
    butones.pack(anchor='w', padx=20, pady=90)
    Button(butones, text="Deposit", font=('verdana', 15), bg='black', fg='white', width=17,
           command=lambda: deposit(found_acc), height=1,
           activebackground='black').grid(row=2,column=0, padx=(15,0), pady=(0,25))
    Button(butones, text="Withdraw", font=('verdana', 15), bg='black', fg='white', width=17,
           command=lambda: withdraw(found_acc), height=1,
           activebackground='black').grid(row=2, column=1, padx=(30,0), pady=(0,25))
    Button(butones, text="Loan", font=('verdana', 15), bg='black', fg='white', width=17,
           command=lambda: loan(found_acc), height=1, activebackground='black').grid(row=2, column=2, padx=(30,0), pady=(0,25))

    Button(butones, text="Account Settings", font=('verdana', 15), bg='black', fg='white', width=17,
           command=lambda: sett(found_acc), height=1, activebackground='black').grid(row=4, column=0, padx=(15,0))
    Button(butones, text="Logout", font=('verdana', 15), bg='black', fg='white', width=17, command=bank_main,
           height=1, activebackground='black').grid(row=4, column=1, padx=(30,0))

load_db()
bank_main()
root.mainloop()