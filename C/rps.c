#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    
    srand(time(NULL));

    printf("Welcome to Rock, Paper, Scissors!\n");
    int userChoice = getUserChoice();
    int computerChoice = getComputerChoice();

    if (userChoice == 1) {
        printf("You chose Rock.\n");
    } else if (userChoice == 2) {
        printf("You chose Paper.\n");
    } else if (userChoice == 3) {
        printf("You chose Scissors.\n");
    } else {
        printf("Invalid choice! Please choose 1, 2, or 3.\n");
        return 1; 
    }
    if (computerChoice == 1) {
        printf("Computer chose Rock.\n");
    } else if (computerChoice == 2) {
        printf("Computer chose Paper.\n");
    } else if (computerChoice == 3) {
        printf("Computer chose Scissors.\n");
    }
    checkWinner(userChoice, computerChoice);

    return 0;
}

int getComputerChoice() {
    return (rand() % 3) + 1; 
}

int getUserChoice() {
    int choice;
    printf("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): ");
    scanf("%d", &choice);
    return choice;
}

void checkWinner(int userChoice, int computerChoice) {
    if (userChoice == computerChoice) {
        printf("It's a tie!\n");
    } else if ((userChoice == 1 && computerChoice == 3) || 
               (userChoice == 2 && computerChoice == 1) || 
               (userChoice == 3 && computerChoice == 2)) {
        printf("You win!\n");
    } else {
        printf("Computer wins!\n");
    }
}