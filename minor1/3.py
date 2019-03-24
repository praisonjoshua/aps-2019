# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:58:46 2019

@author: Praison Joshua
"""
# =============================================================================
# 
# 
# # te=int(input())   
# # for t in range(te):            
# #     N,d=input().split()
# #     n=[str(i) for i in str(N)]
#         
# =============================================================================
import sys 
def getPairsCount(dp, n, qwe): 
      
    count = 0 # Initialize result 
  
    # Consider all possible pairs 
    # and check their sums 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if dp[i] + dp[j] == qwe: 
                count += 1
      
    return count 

inp=input()
inp=int(inp)
d=list()
ds=list()
x=list()
dp=list()
vowels="aeiou"
only_vowels=list()

for i in range(inp):
    d.append(input())
    only_vowels=[each for each in d[i] if each in vowels] 
    x.append(list(set(only_vowels)))
    print(x)
     
    
    
qwe=531
                    
# =============================================================================
# 
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
# =============================================================================

# fullMask = 2**5-1
# cntMask = [0 for _ in range(fullMask+1)]
# print(cntMask)

# for s in p:
#     mask = 0
#     h=len(s)
#     for c in range(h):
#         mask |= 1 << c
#         print(mask)
#     cntMask[mask] += 1

# res = 0
# for i in range(fullMask+1):
#     for j in range(i+1, fullMask+1):
#         if i | j == fullMask:
#             res += cntMask[i] * cntMask[j]

# res += cntMask[fullMask] * (cntMask[fullMask]-1) / 2
# print(res)

print(dp)
n=len(dp)
print(getPairsCount(dp,n, qwe))

   
    

        
    
    



