# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:46:45 2019

@author: Praison Joshua
"""


# =============================================================================
# t=input()
# t=int(t)
# 
# for i in range(t): 
# =============================================================================
#N,d=input().split()
t=int(input())   
for t in range(te):
    N,d=input().split()
    n=[int(i) for i in str(N)]
    #print(n)
    sum=str()
    a=list()
    u=len(n)
    for i in range(u):
        sum=sum+str(n[i])
        a.append(sum+str(d*((u-1)-i)))
    #print(n)
    #print(a)
    a.sort()   
    print(a[0])
    
   
  
    
  
    