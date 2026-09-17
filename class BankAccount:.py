import os

import time

def clear_screen():
  os.system('cls' if os.name=='nt'else 'clear') 

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def drucker(self):
        print(f"Name: {self.owner}")
        print(f"Balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("The amount must be greater than 0")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"${amount} successfully withdrawn. Remaining balance: ${self.balance}")
        else:
            print("Sorry, the amount is unavailable or the balance is insufficient!")

    def get_balance(self):
        print(f"Account owner: {self.owner} | Current balance: ${self.balance}")


def frag():
    owner = input("Enter your name: ")
    
    while True:
        try:
            balance = float(input("Enter your initial balance: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for balance.")
            
    return BankAccount(owner, balance)


# --- حلقة التحكم بالحساب البنكي ---
def account_menu(user_account):
    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                amt = float(input("Enter deposit amount: "))
                user_account.deposit(amt)
                time.sleep(2)
                
            except ValueError:
                print("Invalid amount! Please enter numbers only.")

        elif choice == '2':
            try:
                amt = float(input("Enter withdrawal amount: "))
                user_account.withdraw(amt)
                time.sleep(2)
            except ValueError:
                print("Invalid amount! Please enter numbers only.")

        elif choice == '3':
            user_account.get_balance()
            time.sleep(2)

        elif choice == '4':
            print("Logging out from account...")
            
        else:
            print("Invalid option! Please select from 1 to 4.")
            time.sleep(2)
            


# --- بداية تشغيل البرنامج الرئيسي ---
formation = []

while True:
    qua = input("\nDo you want to create an account? (yes/no): ").lower()
    
    if qua == 'yes':
        user_account = frag()
        formation.append(user_account)
        print("\nAccount created successfully!")
        
        
        # الانتقال المباشر لقائمة خيارات الحساب الجديد
        account_menu(user_account)
        
    elif qua == 'no':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid option, please type 'yes' or 'no'.")