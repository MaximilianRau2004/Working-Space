#include <stdio.h>

int main() {
 
    /** 
    FILE *pFile = fopen("output.txt", "w");

    char text[] = "Hello, World!\nWhats up?\n";

    if (pFile == NULL) {
        perror("Error opening file");
        return 1;
    }

    fprintf(pFile, "%s", text);

    printf("File written successfully.\n");

    fclose(pFile);
    */

    FILE *pFile = fopen("output.txt", "r");

    char buffer[1024] = {0};

    if (pFile == NULL) {
        perror("Error opening file");
        return 1;
    }

    while (fgets(buffer, sizeof(buffer), pFile) != NULL) {
        printf("%s", buffer);
    }

    fclose(pFile);

    return 0;
}

