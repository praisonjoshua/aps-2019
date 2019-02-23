# Python program for Optimized Dynamic Programming solution to 
n = 5
k = 2


C = [0 for i in range(k+1)] 
C[0] = 1 

for i in range(1,n+1): 

    j = min(i ,k) 
    while (j>0): 
        print("j: "+str(j))
        C[j] = C[j] + C[j-1] 
        print("j: "+str(j)+" "+str(C[j]))
        print(C[j])
        print("-----------------")
        j -= 1





print (C)
