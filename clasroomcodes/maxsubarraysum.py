# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:42:09 2019

@author: Praison Joshua
"""


a=[-2,-3,4,-1,-2,1,5,-3]

size=len(a)
max_ending_here = 0
max_so_far=0
for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0 
            
print(max_so_far)            