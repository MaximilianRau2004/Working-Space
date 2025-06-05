#include <stdio.h>

int main() {

    char choice = '\0';
    float fahrenheit = 0.0f;
    float celsius = 0.0f;

    printf("Choose a conversion:\n");
    printf("F for Fahrenheit to Celsius\n");
    printf("C for Celsius to Fahrenheit\n");
    printf("Enter your choice (C or F): ");
    scanf(" %c", &choice);
    if (choice == 'F' || choice == 'f') {
        printf("Enter temperature in Fahrenheit: ");
        scanf("%f", &fahrenheit);
        celsius = (fahrenheit - 32) * 5.0f / 9.0f;
        printf("%.2f Fahrenheit is %.2f Celsius\n", fahrenheit, celsius);
    } else if (choice == 'C' || choice == 'c') {
        printf("Enter temperature in Celsius: ");
        scanf("%f", &celsius);
        fahrenheit = celsius * 9.0f / 5.0f + 32;
        printf("%.2f Celsius is %.2f Fahrenheit\n", celsius, fahrenheit);
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}