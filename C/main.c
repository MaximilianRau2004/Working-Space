#include <stdio.h>
#include <stdlib.h>

int main() {

    /** 
    int number = 0;
    printf("Enter the number of grades: ");
    scanf("%d", &number);

    char *grades = malloc(number * sizeof(char));

    if (grades == NULL) {
        printf("Memory allocation failed.\n");
        return 1; 
    }

    for(int i = 0; i < number; i++) {
        printf("Enter grade %d: ", i + 1);
        scanf(" %c", &grades[i]); 
    }

    for(int i = 0; i < number; i++) {
        printf("Grade %d: %c\n", i + 1, grades[i]);
    }

    free(grades); // deallocate memory
    grades = NULL; // avoids dangling pointer
    */

    int number = 0;
    printf("Enter the number of players: ");
    scanf("%d", &number);

    int *scores = calloc(number, sizeof(int));

    if(scores == NULL) {
        printf("Memory allocation failed.\n");
        return 1; 
    }

    for(int i = 0; i < number; i++) {
        printf("Enter score for player %d: ", i + 1);
        scanf("%d", &scores[i]);
    }

    for(int i = 0; i < number; i++) {
        printf("Score for player %d: %d\n", i + 1, scores[i]);
    }

    free(scores);
    scores = NULL;

    return 0;
}


 