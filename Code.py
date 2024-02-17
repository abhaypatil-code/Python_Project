class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} INR")
        return f"Deposited {amount} INR successfully. Current balance: {self.balance} INR"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn {amount} INR")
        return f"Withdrawn {amount} INR successfully. Current balance: {self.balance} INR"

    def transfer(self, amount, recipient):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        recipient.balance += amount
        self.transaction_history.append(f"Transferred {amount} INR to {recipient.user_id}")
        return f"Transferred {amount} INR to {recipient.user_id}. Current balance: {self.balance} INR"

    def get_transaction_history(self):
        return self.transaction_history

class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, pin):
        self.users[user_id] = User(user_id, pin)

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            return self.users[user_id].authenticate(user_id, pin)
        return False

    def get_user(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        return None


def main():
    atm = ATM()

    # Adding users (You can add more users here)
    atm.add_user("user1", "1234")
    atm.add_user("user2", "5678")

    while True:
        print("\nWelcome to the ATM system")
        user_id = input("Enter user ID: ")
        pin = input("Enter PIN: ")

        if atm.authenticate_user(user_id, pin):
            current_user = atm.get_user(user_id)
            print(f"Authentication successful. Welcome, {user_id}!")

            while True:
                print("\nChoose an option:")
                print("1. Transactions History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Quit")

                choice = input("Enter your choice: ")
                
                if choice == "1":
                    print("Transaction History:")
                    for transaction in current_user.get_transaction_history():
                        print(transaction)

                elif choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    print(current_user.withdraw(amount))

                elif choice == "3":
                    amount = float(input("Enter amount to deposit: "))
                    print(current_user.deposit(amount))

                elif choice == "4":
                    recipient_id = input("Enter recipient's user ID: ")
                    amount = float(input("Enter amount to transfer: "))
                    recipient = atm.get_user(recipient_id)
                    if recipient:
                        print(current_user.transfer(amount, recipient))
                    else:
                        print("Recipient not found.")

                elif choice == "5":
                    print("Thank you for using the ATM. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid user ID or PIN. Please try again.")


if __name__ == "__main__":
    main()

# This Code Belongs to Abhay Patil
# linkedin Profile : https://www.linkedin.com/in/abhaypatil014/