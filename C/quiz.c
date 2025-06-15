#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    
    char questions[][100] = {
        "What is the capital of France?",
        "What is 2 + 2?",
        "What is the largest planet in our solar system?",
        "Who painted the Mona Lisa?",
        "What is the boiling point of water in Celsius?"
    };

    char options[][100] = {
        "A) Paris\nB) London\nC) Berlin\nD) Madrid",
        "A) 3\nB) 4\nC) 5\nD) 6",
        "A) Earth\nB) Mars\nC) Jupiter\nD) Saturn",
        "A) Vincent van Gogh\nB) Pablo Picasso\nC) Leonardo da Vinci\nD) Claude Monet",
        "A) 90°C\nB) 100°C\nC) 80°C\nD) 120°C"
    };

    char answerKey[] = {'A', 'B', 'C', 'C', 'B'};

    int score = 0;
    int numQuestions = sizeof(questions) / sizeof(questions[0]);
    printf("Welcome to the Quiz Game!\n");
    for (int i = 0; i < numQuestions; i++) {
        printf("\nQuestion %d: %s\n", i + 1, questions[i]);
        printf("%s\n", options[i]);
        
        char answer;
        printf("\nYour answer (A/B/C/D): ");
        scanf(" %c", &answer);

        answer = toupper(answer); 
        if (answer < 'A' || answer > 'D') {
            printf("Invalid answer! Please enter A, B, C, or D.\n");
            i--; 
            continue;
        }
        
        if (answer == answerKey[i]) {
            printf("Correct!\n");
            score++;
        } else {
            printf("Wrong! The correct answer was %c.\n", answerKey[i]);
        }
    }
    printf("\nYour total score is: %d out of %d\n", score, numQuestions);

    return 0;
}