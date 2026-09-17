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


# --- 1. Function to save accounts to a file ---
def save_accounts(formation):
    with open("accounts.txt", "w") as file:
        for acc in formation:
            file.write(f"{acc.owner},{acc.balance}\n")
    print("-> Data saved to file successfully!")


# --- 2. Function to load accounts from the file ---
def load_accounts():
    formation = []
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 2:
                    name = data[0]
                    balance = float(data[1])
                    acc = BankAccount(name, balance)
                    formation.append(acc)
        print("-> Previous accounts loaded successfully!")
    except FileNotFoundError:
        print("-> No existing data file found. A new one will be created upon saving.")
    
    return formation


# --- 3. Function to search/find an existing account by name ---
def find_account(owner_name, formation):
    for acc in formation:
        if acc.owner.lower() == owner_name.lower():
            return acc
    return None


# --- Function to create account with input validation ---
def frag():
    owner = input("Enter your name: ")
    
    while True:
        try:
            balance = float(input("Enter your initial balance: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for balance.")
            
    return BankAccount(owner, balance)


# --- Account Control Menu ---
def account_menu(user_account, formation):
    while True:
        print(f"\n--- Welcome {user_account.owner} ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                amt = float(input("Enter deposit amount: "))
                user_account.deposit(amt)
                save_accounts(formation)
            except ValueError:
                print("Invalid amount! Please enter numbers only.")

        elif choice == '2':
            try:
                amt = float(input("Enter withdrawal amount: "))
                user_account.withdraw(amt)
                save_accounts(formation)
            except ValueError:
                print("Invalid amount! Please enter numbers only.")

        elif choice == '3':
            user_account.get_balance()

        elif choice == '4':
            print("Logging out from account...")
            break
        else:
            print("Invalid option! Please select from 1 to 4.")


# --- Main Program Execution ---

formation = load_accounts()

while True:
    print("\n=== Main Menu ===")
    print("1. Login to Existing Account")
    print("2. Create New Account")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")

    if choice == '1':
        search_name = input("Enter your account name: ")
        found_acc = find_account(search_name, formation)
        
        if found_acc:
            print(f"\nAccount found! Logging in...")
            account_menu(found_acc, formation)
        else:
            print("\nAccount not found! Please check the name or create a new account.")

    elif choice == '2':
        user_account = frag()
        formation.append(user_account)
        print("\nAccount created successfully!")
        
        save_accounts(formation)
        account_menu(user_account, formation)

    elif choice == '3':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid option, please type 1, 2, or 3.")