#include <stdio.h>
#include <stdbool.h>
#include <string.h>
 
typedef struct {
    char name[50];
    int age;
    float gpa;
    bool isFullTime;
} Student ;

int main() {
    
    Student student1 = {"Alice", 20, 3.8, true};
    Student student2 = {"Bob", 22, 3.5, false};
    Student student3 = {0}; 

    strcpy(student3.name, "Charlie");

    printf("Student 1: %s, Age: %d, GPA: %.2f, Full-time: %s\n", 
           student1.name, student1.age, student1.gpa, 
           student1.isFullTime ? "Yes" : "No");
    printf("Student 2: %s, Age: %d, GPA: %.2f, Full-time: %s\n",
           student2.name, student2.age, student2.gpa, 
           student2.isFullTime ? "Yes" : "No");
    printf("%s", student3.name);

    return 0;
}