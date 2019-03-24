#include<stdio.h>
#include<math.h>



int main()
{
    int n,m,sum;
     int  i,j,a,b,c=0;
    
    scanf("%d",&n);
    int arr[n];
    for (i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
        
    }
    
   // scanf("%d",&m);
    int q[2];
    
    
    int set_size = n ;
    unsigned int size = pow(2,set_size) ;

    for (i=0; i<size;i++)
    {
         printf("\n")   ;
     sum=0;
     c=0;
        for (j=0;j<set_size;j++)
        {
           
          
            if (i&(1<<j))
            {
            
            
             sum = sum+arr[j];
             
			 c++;
             q[1]=q[0];
			 q[0]=j;
			 
		
			 
			 
			 
            printf("%d\t",arr[j]);
             
             
         
          
                
                
                
                
            }
            
        
    
        
    }       
    }
        
}
