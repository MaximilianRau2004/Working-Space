#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void birthday(int* age);

int main() {
 
    int age = 25;
    int *pAge = &age;

    birthday(pAge);
    printf("Age: %d\n", age);

    printf("%p\n", &age); 

    printf("%p\n", pAge);

    return 0;
}

void birthday(int* age) {
    (*age)++;
}
 