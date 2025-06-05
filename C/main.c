#include <stdio.h>

int main() {

    char name[] = "John Doe";
    name[1] = 'a'; 
    printf("Hello, %s!\n", name);

    return 0;
}