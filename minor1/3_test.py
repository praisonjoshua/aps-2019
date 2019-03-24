from itertools import combinations
p=[]
de=[]
te=int(input())   
for t in range(te): 
    n = int(input())
    for i in range(n):
        d=input()
        d=list(d)
        d=set(d)
        d=list(d)
        d=sorted(d)
        de.append(d)
       
    l=[]
    dp=dict()
  
    for i in range(1,6):
        for j in combinations(sorted(set("aeiou")),i):
            dp[j]=0
      
            k=list(j)
            if k in de:
                sum=0
                for x in range(len(k)):
                    
                    if de[1]=="a":
                        sum=sum+16
                    elif ke[2]=="e":
                        sum=sum+8
                    elif ke[3]=="i":
                        sum=sum+4
                    elif ke[4]=="o":
                        sum=sum+2   
                    elif ke[5]=="u":
                        sum=sum+1
    print(dp)                
                               
    
    # count=0
    # lis=list(dp.keys())     
    # #for i in range(1,len("aeiou")+1):
    # for i in range(len(lis)):
    #     for j in range(1,len(lis)):
    #         val=dp[lis[i]]|dp[lis[j]]
    #         if val==31:
    #             count=count+1
    # res=count/2
    # res=int(res)
    # print(res) 