class Atm:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.generate_pin()

    def generate_pin(self):
        self.pin = int(input("Set your PIN: "))

    def menu(self):
        options = {
            1: ("Deposit Money", self.deposit),
            2: ("Withdraw Money", self.withdraw),
            3: ("Check Balance", self.check_balance),
            4: ("Change PIN", self.change_pin),
            5: ("Quit", self.quit_atm)
        }

        while True:
            print("\n--- ATM Menu ---")
            for k, (label, _) in options.items():
                print(f"{k}. {label}")

            try:
                choice = int(input("Choose option: "))
                if choice in options:
                    callback = options[choice][1]  
                    callback()                     
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number!")

    
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def change_pin(self):
        new_pin = int(input("Enter new PIN: "))
        self.pin = new_pin
        print("PIN changed successfully!")

    def quit_atm(self):
        print("Thank you for using the ATM!")
        exit()


user1 = Atm("Teja")
user1.menu()