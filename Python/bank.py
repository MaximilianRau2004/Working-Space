
def show_balance(balance):
    print(f"Your balance is: ${balance}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("Invalid amount.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Invalid amount.")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    print("Welcome to your bank account!")
    print("What do you want to do?")
    while is_running:
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            is_running = False

if __name__ == "__main__":
    main()
