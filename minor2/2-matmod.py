# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:44:55 2019

@author: kingdurai
"""

# =============================================================================
# s,c=input().split()
# =============================================================================
s='abb'
c='b'
l=len(s)
l=l-1
cc=0
ni=0
for i in range(l+1):
    if s[i]==c:
       
        bef=i-ni
        bef=bef+1
       
        aft=l-i
       
        cc=cc+bef+(bef*aft)
        
        ni=i+1
    
        
print(cc)        