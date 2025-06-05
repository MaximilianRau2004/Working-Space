#include <stdio.h>

int main() {

    int choice = 0;
    float pounds = 0.0f;
    float kilograms = 0.0f;

    printf("Choose a conversion:\n");
    printf("1 for Pounds to Kilograms\n");
    printf("2 for Kilograms to Pounds\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    if (choice == 1) {
        printf("Enter weight in pounds: ");
        scanf("%f", &pounds);
        kilograms = pounds * 0.453592;
        printf("%.2f pounds is %.2f kilograms\n", pounds, kilograms);
    } else if (choice == 2) {
        printf("Enter weight in kilograms: ");
        scanf("%f", &kilograms);
        pounds = kilograms / 0.453592;
        printf("%.2f kilograms is %.2f pounds\n", kilograms, pounds);
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}