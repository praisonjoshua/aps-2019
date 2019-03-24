# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:39:54 2019

@author: Praison Joshua
"""
import numpy as np
tot=0
n=int(input())
d=[0 for k in range(5)]
vowel=[0 for k in range(32)]
for i in range(n):
    st=input()
    st=set(st)
    st=list(st)
    tot=0
    d=[0 for k in range(5)]
    for j in range(len(st)):
        
        if st[j]=='a':
            d[0]=16
        if st[j]=='e':
            d[1]=8    
        if st[j]=='i':
            d[2]=4
        if st[j]=='o':
            d[3]=2    
        if st[j]=='u':
            d[4]=1    
    qwe=sum(d) 
    tot=tot+qwe    
    vowel[d[0]|d[1]|d[2]|d[3]|d[4]]=vowel[d[0]|d[1]|d[2]|d[3]|d[4]]+1

count=0
   
for i in range(32):
    if vowel[i]==0:
        continue
    for j in range(i+1,32):
        if vowel[j]==0:
            continue
        if i|j==31:
            count=count+(vowel[i]*vowel[j])
        
r=vowel[31]

res=(r*(r-1))/2

finalised=count+res
finalised=int(finalised)
print(finalised)    