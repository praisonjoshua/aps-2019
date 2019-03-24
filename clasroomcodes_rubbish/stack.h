#include <stdio.h>
#include <stdlib.h>

#define STACKSIZE 5
#define TRUE 1
#define FALSE 0



struct stack
{
    int top;
    int items[STACKSIZE];
};
typedef struct stack STACK;


int full(STACK *S)
{
    if(S->top == STACKSIZE-1)
        return TRUE;
    else
        return FALSE;
}

void push(STACK *S)
{
    if(full(S)){
        printf("Stack full\n");
        
        return;
    }

    int x;
    printf("Enter the item to be pushed\n");
    scanf("%d", &x);

    S->top++;
    S->items[S->top] = x;

}

int empty(STACK * S)
{
   if(S->top == -1)
        return TRUE;
   else
        return FALSE;
}
void pop(STACK *S)
{
    if(empty(S)){
        printf("Stack Empty\n");
        return;
    }

    int x;
    x = S->items[S->top];
    printf("Popped item is %d\n", x);
    S->top--;
}

void peek(STACK *S)
{
    if(empty(S)){
        printf("Stack Empty\n");
        return;
    }

    int x;
    x = S->items[S->top];
    printf("Peeked item is %d\n", x);
}

void print(STACK *S)
{
    if(empty(S)){
        printf("Stack Empty\n");
        return;
    }

    int i;
    for(i = S->top; i >= 0; i--)
        printf("| %d |\n", S->items[i]);
}
