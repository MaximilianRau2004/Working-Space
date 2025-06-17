#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef int Number;
typedef char String[];

typedef enum {
    MONDAY = 1,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
} DayOfWeek ;

int main() {
    
    Number x = 5;
    Number y = 10;
    Number z = x + y;
    printf("The sum of %d and %d is %d\n", x, y, z);

    String greeting = "Hello, World!";
    printf("%s\n", greeting);

    DayOfWeek today = SUNDAY;
    printf("Today is day number %d of the week.\n", today);

    return 0;
}
 
