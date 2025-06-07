#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {

    int a, b;
    char operation;

    printf("Geben sie bitte die erste Zahl ein: ");
    scanf("%d", &a);

    printf("Wählen sie bitte eine Operation (+, -, *, /, %%, !, ^ (power), s (square root)): ");
    scanf(" %s", &operation);
    if (operation == '!') {
        printf("Das Ergebnis von %d! ist %d\n", a, factorial(a));
        return 0; 
    } else if (operation == 's') {
        printf("Die Quadratwurzel von %d ist %d\n", a, square_root(a));
        return 0; 
    } else {
        printf("Geben sie bitte die zweite Zahl ein: ");
        scanf("%d", &b);
        switch(operation) {
            case '+':
                printf("Das Ergebnis von %d + %d ist %d\n", a, b, add(a, b));
                break;
            case '-':
                printf("Das Ergebnis von %d - %d ist %d\n", a, b, subtract(a, b));
                break;
            case '*':
                printf("Das Ergebnis von %d * %d ist %d\n", a, b, multiply(a, b));
                break;
            case '/':
                printf("Das Ergebnis von %d / %d ist %d\n", a, b, divide(a, b));
                break;
            case '%':
                printf("Das Ergebnis von %d %% %d ist %d\n", a, b, modulus(a, b));
                break;
            case '^':
                printf("Das Ergebnis von %d ^ %d ist %d\n", a, b, power(a, b));
                break;
            default:
                printf("Ungültige Operation!\n");
        }
    }
    return 0;
}

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    int x = a;
    for (int i = 1; i < b; i++) {
        x += a; 
    }
    return x;
}

int divide(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero is not allowed.\n");
        return 0; 
    }
    int result = 0;
    while (a >= b) {
        a -= b;
        result++; 
    }
}

int modulus(int a, int b) {
    if (b == 0) {
        printf("Error: Division by zero is not allowed.\n");
        return 0; 
    }

    return a - (b * (a / b));
}

int power(int base, int exponent) {
    int result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

int square_root(int a) {
    if (a < 0) {
        printf("Error: Cannot compute square root of a negative number.\n");
        return -1; 
    }
    if (a == 0 || a == 1) {
        return a; 
    }

    int start = 0, end = a, mid;
    while (start <= end) {
        mid = (start + end) / 2;
        if (mid * mid == a) {
            return mid; 
        } else if (mid * mid < a) {
            start = mid + 1; 
        } else {
            end = mid - 1; 
        }
    }
    return mid; 
}

int factorial(int n) {
    if (n < 0) {
        printf("Error: Factorial of a negative number is not defined.\n");
        return -1; 
    }
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
