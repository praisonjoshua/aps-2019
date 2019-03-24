#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    long long int t;
    scanf("%lld",&t);
    long long int i,j;
    
    long long int vowel[32];
    memset(vowel,0,sizeof(vowel));
    while(t--)
    {
        long long int n,count=0,d[5],sum=0;
        memset(d,0,sizeof(d));
        
        scanf("%lld",&n);
        char str[30000000];
        for(i=0;i<n;i++)
        {
            scanf("%s",str);
              for(j=0;str[j]!='\0';j++)
            {
                if(str[j]=='a')
                    d[0]=16;
                if(str[j]=='e')
                    d[1]=8;
                if(str[j]=='i')
                    d[2]=4;
                if(str[j]=='o')
                    d[3]=2;
                if(str[j]=='u')
                    d[4]=1;
            }
            for(j=0;j<5;j++)
            {
                sum+=d[j];
            }
          //  printf("%lld\n",sum);
            vowel[d[0]|d[1]|d[2]|d[3]|d[4]]++;
            
         //printf("%d\n",vowel[d[0]+d[1]+d[2]+d[3]+d[4]]);
            memset(d,0,sizeof(d));
            sum=0;
        
                
        }
        for(i=1;i<32&&vowel[i]>=0;i++)
        {//printf("%d ",vowel[i]);
            for(j=i+1;j<32&&vowel[j]>=0;j++)
            {//printf("%d ",vowel[j]);
                if((i|j)==31)
               {
                    count+=(vowel[i]*vowel[j]);
                }
            }
        }
        long long int r=vowel[31];
        long long int res=(r*(r-1))/2;
        printf("%lld\n",count+res);
        count=0;
        memset(vowel,0,sizeof(vowel));
        //for(i=0;str[i]!='\0';i++)
        //{
    
    }return 0;
}
