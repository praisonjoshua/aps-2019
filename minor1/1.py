# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:23:13 2019

@author: Praison Joshua
"""

t=input()
t=int(t)

for i in range(t):    
    n=input()
    x = [int(x) for x in input().strip().split(' ')]
    maxflag=0
    minflag=1
    
    only_pos = [num for num in x if num >= 0]
    only_neg = [num for num in x if num < 0]
    
    sumn=sum(only_neg)
    sump=sum(only_pos)    

    p=len(only_pos)
    q=len(only_neg)
    xl=len(x)
    if p==xl:
        print(p,p)
    elif q==xl:
        print(q,q)
    else:
        print(p,q)
        
# =============================================================================
#     if sump>=sump:
#         max=p
#         min=q
#         maxflag=1
#         if sumn==sump:
#             print(max,min)
#         else:
#             print(max,max)  
#     else:
#         min=p
#         max=q
#         minflag=1
#         if sumn==sump:
#             if min==0:
#                 print(max,max)
#             print(max,min)
#         else:
#             print(max,max)  
#       
# =============================================================================
    
    
    
   
    
    
    