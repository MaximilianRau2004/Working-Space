#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    
    srand(time(NULL));

    int min = 1;
    int max = 6;

    int random_number = (rand() % max) + min; 
    printf("Random number generated: %d\n", random_number);

    return 0;
}

