#include <stdio.h>
#include <string.h>

int main() {
    
    char item[50] = " ";
    float price = 0.0f;
    int quantity = 0;
    char currency = '$';
    float total = 0.0f;

    printf("Enter item name: ");
    fgets(item, sizeof(item), stdin);
    item[strlen(item) - 1] = '\0'; 

    printf("What is the price of the item? ");
    scanf("%f", &price);

    printf("How many items do you want to buy? ");
    scanf("%d", &quantity);

    total = price * quantity;

    printf("You have bought %d %s/s\n", quantity, item);
    printf("The total price is: %c%.2f\n", currency, total);

    return 0;
}