#include <stdio.h>
#include <string.h>

int main() {

    int age = 0;
    float gpa = 0.0f;
    char grade = '\0';
    char name[30] = "";

    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter your GPA: ");
    scanf("%f", &gpa);

    printf("Enter your grade (A, B, C, D, F): ");
    scanf(" %c", &grade);

    getchar();
    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0'; 

    printf("Your age is %d\n", age);
    printf("Your GPA is %.2f\n", gpa);
    printf("Your grade is %c\n", grade);
    printf("Your name is %s\n", name);

    return 0;
}