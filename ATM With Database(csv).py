import random
import csv
import os

bank_accounts = []
database_file = "mabuhay_database.csv"

class BankAccount:
    def __init__(self, name, acc_number, pin, balance):
        self.name = name
        self.acc_number = acc_number
        self.pin = pin
        self.balance = balance

def upd_db():
    with open(database_file, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Account Number", "PIN", "Balance"])
        for acc in bank_accounts:
            csv_writer.writerow([acc.name, acc.acc_number, acc.pin, acc.balance])
    print("Data successfully saved!")

def load_db():
    if os.path.isfile(database_file):
        try:
            with open(database_file, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader, None)
                for row in csv_reader:
                    if row:
                        load_accs = BankAccount(row[0], int(row[1]), int(row[2]), float(row[3]))
                        bank_accounts.append(load_accs)
                print(f"Successfully loaded {len(bank_accounts)} account!")
        except FileNotFoundError:
            print("ERROR! File doesn't exist!")

def bank_main():
    load_db()
    while True:
        print("""
----WELCOME TO MABUHAY BANK----
1. Create an account
2. Login into your account
3. Exit""")
        try:
            choose = int(input("Choose an option (1-3): "))
            if choose == 1:
                bank_create()
            elif choose == 2:
                bank_login()
            elif choose == 3:
                print("Exiting...")
                break
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def bank_create():
    print("----CREATE BANK ACCOUNT----")
    while True:
        last = input("Last Name: ")
        first = input("First Name: ")
        if last.replace(" ","").isalpha() and first.replace(" ","").isalpha():
            name = f"{first} {last}"
            break
        else:
            print("Invalid name, input letters only.")

    while True:
        pin = (input("Enter 4-digit PIN: "))
        if pin.isdigit() and len(pin) == 4:
            pin = int(pin)
            break
        else:
            print("Invalid, 4-digit PIN is required.")

    while True:
        try:
            balance = input("Your balance is ZERO. Enter ₱20,000 initial deposit: ")
            balance = float(balance.replace(",", ""))
            if balance >= 20000:
                break
            else:
                print("₱20,000 is the minimum initial deposit.")
        except ValueError:
            print("Invalid input, try again.")

    while True:
        check = input("Confirm account registration? (Y/N): ").lower()
        if check == "y":
            acc_number = random.randint(1000000, 9999999)
            new_bank = BankAccount(name, acc_number, pin, balance)
            bank_accounts.append(new_bank)

            upd_db()

            print(f"""
Welcome {name}, your account is successfully created!
Your account number is {acc_number} 
Account balance is {balance}""")
            break
        elif check == "n":
            print("Account registration cancelled.")
            break
        else:
            print("Invalid input, try again.")

def bank_login():
    while True:
        if len(bank_accounts) == 0:
            print("No accounts created.")
            break
        else:
            print("----LOGIN INTO YOUR MABUHAY BANK ACCOUNT----")
            while True:
                login_id = input("Enter 7-digit account number (0 to back): ")
                if login_id == "0":
                    return
                elif login_id.isdigit() and len(login_id) == 7:
                    login_id = int(login_id)
                    break
                else:
                    print("Invalid input, try again.")
            found_acc = False
            for acc in bank_accounts:
                if acc.acc_number == login_id:
                    found_acc = True
                    while True:
                        pin_input = input("Enter 4-digit PIN (0 to cancel): ")
                        if pin_input == "0":
                            break
                        elif not pin_input.isdigit() or len(pin_input) != 4:
                            print("4-digit PIN only, try again.")
                            continue
                        if int(pin_input) == acc.pin:
                            print(f"Login successful. Welcome, {acc.name}!")
                            atm(acc)
                            return
                        else:
                            print("PIN does not match, try again!")
            if not found_acc:
                print("Account not found, try again.")

def deposit(acc):
    print("""
Per Transaction
Minimum: ₱10,000
Maximum: ₱500,000""")
    while True:
        try:
            bank_deposit = input("Enter amount (0 to cancel): ")
            if bank_deposit == "0":
                return
            bank_deposit = float(bank_deposit.replace(",", ""))
            if 10000 <= bank_deposit <= 500000:
                acc.balance = acc.balance + bank_deposit
                print(f"Your account balance is now {acc.balance}.")
                break
            else:
                print("Invalid amount, try again.")
        except ValueError:
            print("Invalid input, numbers only.")
    upd_db()

def withdraw(acc):
    print("""
Per Transaction
Minimum: ₱5,000
Maximum: ₱50,000""")
    while True:
        try:
            bank_withdraw = input("Enter amount (0 to cancel): ")
            if bank_withdraw == "0":
                return
            bank_withdraw = float(bank_withdraw.replace(",", ""))
            if bank_withdraw > acc.balance:
                print("Insufficient balance, try again.")
            elif 5000 <= bank_withdraw <= 50000:
                acc.balance = acc.balance - bank_withdraw
                print(f"Your account balance is now {acc.balance}.")
                break
            else:
                print("Invalid amount, try again.")
        except ValueError:
            print("Invalid input, numbers only.")
    upd_db()

def verify(acc):
    while True:
        try:
            check = int(input("Enter your PIN (0 to exit): "))
            if check == acc.pin:
                return True
            elif check == 0:
                print("Exiting...")
                return False
            else:
                print("Incorrect PIN, try again.")
        except ValueError:
            print("Invalid input, try again.")

def account_settings(acc):
    while True:
        print("""
----ACCOUNT SETTINGS----
1. Change PIN
2. Delete Account
3. Back""")
        try:
            choice3 = int(input("Select an option (1-3): "))
            if choice3 == 1:
                if verify(acc):
                    while True:
                        new_pin = input("Set new PIN: ")
                        if new_pin.isdigit() and len(new_pin) == 4:
                            acc.pin = int(new_pin)
                            upd_db()
                            print("PIN successfully changed.")
                            break
                        else:
                            print("Invalid PIN format, try again.")
            elif choice3 == 2:
                if verify(acc):
                    conf = input("WARNING! Do you want to continue? (Y/N): ").lower()
                    if conf == "y":
                        bank_accounts.remove(acc)
                        upd_db()
                        print("Account successfully deleted.")
                        break
                    elif conf == "n":
                        print("Returning...")
                    else:
                        print("Invalid input, try again.")
            elif choice3 == 3:
                break
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, try again.")

def atm(acc):
    while True:
        print(f"""
----WELCOME {acc.name}----
1. Check balance
2. Deposit
3. Withdraw
4. Account settings
5. Back""")
        try:
            choose2 = int(input("Choose an option (1-5): "))
            if choose2 == 1:
                print(f"{acc.name}, your account balance: {acc.balance}")
            elif choose2 == 2:
                deposit(acc)
            elif choose2 == 3:
                withdraw(acc)
            elif choose2 == 4:
                account_settings(acc)
                if acc not in bank_accounts:
                    break
            elif choose2 == 5:
                print("Exiting...")
                break
            else:
                print("Invalid input (1-5), try again.")
        except ValueError:
            print("Invalid input, try again.")

bank_main()
