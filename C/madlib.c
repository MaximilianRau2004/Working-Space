#include <stdio.h>
#include <string.h>

int main() {
    
    char noun[50] = " ";
    char verb[50] = " ";
    char adjective1[50] = " ";
    char adjective2[50] = " ";
    char adjective3[50] = " ";
    
    printf("Enter an adjecctive: ");
    fgets(adjective1, sizeof(adjective1), stdin);
    adjective1[strlen(adjective1) - 1] = '\0'; 

    printf("Enter another noun: ");
    fgets(noun, sizeof(noun), stdin);
    noun[strlen(noun) - 1] = '\0';

    printf("Enter another adjective: ");
    fgets(adjective2, sizeof(adjective2), stdin);
    adjective2[strlen(adjective2) - 1] = '\0';

    printf("Enter a verb: ");
    fgets(verb, sizeof(verb), stdin);
    verb[strlen(verb) - 1] = '\0';

    printf("Enter a adjective: ");
    fgets(adjective3, sizeof(adjective3), stdin);
    adjective3[strlen(adjective3) - 1] = '\0';

    printf("The %s %s is %s and it can %s very %s.\n", adjective1, noun, adjective2, verb, adjective3);

    return 0;
}