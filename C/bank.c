#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void checkBalance(float balance);
float deposit(float balance, float amount);
float withdraw(float balance, float amount);

int main() {
    
    int choice;
    float balance = 0.0;
    float amount = 0.0;

    printf("Welcome to the Bank Management System!\n");
    printf("1. Check Balance\n");
    printf("2. Deposit Funds\n");
    printf("3. Withdraw Funds\n");
    printf("4. Exit\n");
    printf("Please enter your choice: ");
    scanf("%d", &choice);
    while (choice != 4) {
        switch (choice) {
            case 1:
                checkBalance(balance);
                break;
            case 2:
                printf("Enter amount to deposit: ");
                scanf("%f", &amount);
                balance = deposit(balance, amount);
                break;
            case 3:
                printf("Enter amount to withdraw: ");
                scanf("%f", &amount);
                balance = withdraw(balance, amount);
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
        printf("Please enter your choice: ");
        scanf("%d", &choice);
    }

    return 0;
}

void checkBalance(float balance) {
    if (balance < 0) {
        printf("Your balance is negative! Please deposit funds.\n");
    } else {
        printf("Your current balance is: $%.2f\n", balance);
    }
}

float deposit(float balance, float amount) {
    if (amount <= 0) {
        printf("Invalid deposit amount! Please enter a positive value.\n");
        return balance;
    }
    balance += amount;
    printf("You have deposited $%.2f. New balance: $%.2f\n", amount, balance);
    return balance;
}

float withdraw(float balance, float amount) {
    if (amount <= 0) {
        printf("Invalid withdrawal amount! Please enter a positive value.\n");
        return balance;
    }
    if (amount > balance) {
        printf("Insufficient funds! You cannot withdraw more than your current balance of $%.2f.\n", balance);
        return balance;
    }
    balance -= amount;
    printf("You have withdrawn $%.2f. New balance: $%.2f\n", amount, balance);
    return balance;
}