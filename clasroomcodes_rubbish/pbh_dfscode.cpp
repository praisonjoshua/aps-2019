
#include <stdio.h>
#include <stdlib.h>


int v = 6;


    int m[10][10] =
                    {
                        {0, 1, 1,1, 0, 0},
                        {1, 0, 1, 0, 0,0},
                        {1, 1, 0, 0, 0,0},
                        {1, 0, 0, 0, 0,0},
                        {0, 0, 0,0, 0, 1},
                      { 0, 0,0, 0, 1,0}
                    };



int source = 0;
int c=0;
int visited[10];


void dfs(int m[10][10], int v, int source)
{
  
    int i;

  printf("(%d)",c++);
    visited[source] = 1;

    for(i=0; i<v; i++)
    {
        if(m[source][i] == 1 && visited[i] == 0)
        {
           printf("%d\t", i);
            dfs(m, v, i);
           // printf("(%d)",c++);
        }
        
        if(m[source][i] == 1 && visited[i] == 1)
        {
           printf("%d\t", i);
            dfs(m, v, i);
           // printf("(%d)",c++);
        }
    }
    
}

int main()
{
  
    int i;


    for (i= 0; i < v; i ++)
        visited[i] = 0;


    printf("The DFS Traversal is... \n");
    printf("%d\t", source);
    dfs(m, v, source);

    return 0;
}
