import random
from time import sleep

def spin_row():
    symbols = ['🍉', '🍒', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '⭐':
            return bet * 10
    return 0

def main():
    balance = 100

    print("****************************")
    print("Welcome to the slot machine!")
    print("Symbols:  🍉  🍒  🍋  🔔  ⭐")
    print("****************************")

    while balance > 0:
        print()
        print(f"Current balance: ${balance}")

        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Invalid bet.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds.")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0.")

        balance -= bet
        row = spin_row()
        print("Spinning...")
        sleep(1)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost!")

        balance += payout

        play_again = input("Spin again? (y/n): ")

        if play_again.lower() != "y":
            break

    print("Thanks for playing!")
    print(f"Your final balance is: ${balance}")

if __name__ == "__main__":
    main()

