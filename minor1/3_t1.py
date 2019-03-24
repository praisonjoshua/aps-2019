# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:55:19 2019

@author: Praison Joshua
"""
from itertools import combinations
p=[]
de=[]
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


te=int(input())   
for t in range(te):
    n = int(input())
    for i in range(n):
        d=input()

        d=set(d)
        d=list(d)
        d=sorted(d)

        de.append(d)
       
    l=[]
    dp=dict()

    for i in range(1,6):
        for j in combinations({'a', 'e', 'i', 'o', 'u'},i):
            j=tuple(sorted(j))
            dp[j]=0
            jl=list(j)
            if jl in de:
                cou=de.count(jl)
                dp[j]=cou
            
    #print(dp)
    dval=list(dp.values())
    dkey=list(dp.keys())
    #print(dval)
    #print(n)
    
    fc=0   

    for i in range(31):
        for j in range(i+1,len(31)):
            temp=frozenset(dkey[i]+dkey[j])
            
            if len(temp)==5:
                tval=dval[i]*dval[j]
                fc=fc+tval

 
    # print(fc)
    last=dval[30] 
    final=(last*(last-1))/2
    fc=fc+final
   
        
    
    
   
        
        

    
          
                     
    fc=int(fc)        
    print(fc)
    





