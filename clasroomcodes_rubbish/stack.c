#include <stdio.h>
#include <stdlib.h>
#include "stack.h"




int main()
{
    STACK S;
    S.top = -1;
    int choice=0;

    while(1) {
        printf("\n Menu\n");
        printf("1-PUSH\n");
        printf("2-POP\n");
        printf("3-PEEK\n");
        printf("4-PRINT\n");
        printf("5-EXIT\n");
        printf("Enter your choice\n");
        scanf("%d", &choice);
        switch(choice) {
            case 1: push(&S);
                    break;
            case 2: pop(&S);
                    break;
            case 3: peek(&S);
                    break;
            case 4: print(&S);
                    break;
            case 5: printf("Terminating\n");
                    exit(1);
        }
    }

    return 0;
}


