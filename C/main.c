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

    /**
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
    */

    int number = 0;
    printf("Enter the number of elements: ");
    scanf("%d", &number);

    float *prices = malloc(number * sizeof(float));

    if(prices == NULL) {
        printf("Memory allocation failed.\n");
        return 1; 
    }

    for(int i = 0; i < number; i++) {
        printf("Enter price for item %d: ", i + 1);
        scanf("%f", &prices[i]);
    }

    int newNumber = 0;
    printf("Enter the new number of prices: ");
    scanf("%d", &newNumber);

    float *temp = realloc(prices, newNumber * sizeof(float));

    if(temp == NULL) {
        printf("Memory reallocation failed.\n");
    } else {
        prices = temp; 
        temp = NULL; 

        for(int i = number; i < newNumber; i++) {
        printf("Enter price for item %d: ", i + 1);
        scanf("%f", &prices[i]);
        }

        for(int i = 0; i < newNumber; i++) {
        printf("Price for item %d: %.2f\n", i + 1, prices[i]);
    }
    }

    free(prices); 
    prices = NULL; 

    return 0;
}


 