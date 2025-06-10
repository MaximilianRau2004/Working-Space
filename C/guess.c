#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    
    srand(time(NULL));

    int guess = 0;
    int tries = 0;
    int min = 1;
    int max = 100;
    int answer = (rand() % (max - min + 1)) + min;

    printf("Welcome to the Guessing Game!\n");
    printf("I have selected a number between %d and %d.\n", min, max);
    printf("Try to guess it!\n");
    while (guess != answer) {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        tries++;

        if (guess < min || guess > max) {
            printf("Your guess is out of bounds! Please guess a number between %d and %d.\n", min, max);
        } else if (guess < answer) {
            printf("Too low! Try again.\n");
        } else if (guess > answer) {
            printf("Too high! Try again.\n");
        } else {
            printf("Congratulations! You've guessed the number %d in %d tries!\n", answer, tries);
        }
    }

}