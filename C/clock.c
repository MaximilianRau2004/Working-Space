#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <unistd.h>

int main() {

    time_t rawtime = 0;
    struct tm *pTime = NULL;
    bool isRunning = true;

    printf("Clock Application\n");
    printf("Press Ctrl+C to stop the clock.\n");

    while (isRunning) {
        time(&rawtime); 
        pTime = localtime(&rawtime);
        printf("\r%02d:%02d:%02d", pTime->tm_hour, pTime->tm_min, pTime->tm_sec);
        fflush(stdout); 
        sleep(1);
    }

    return 0;
}