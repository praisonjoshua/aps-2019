# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:11:20 2019

@author: Praison Joshua
"""






def binomialCoef(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
         
            if j == 0 or j == i: 
                C[i][j] = 1
  
    
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
  
    print(C)
    return(C[n][k])

n = 10
k = 5
print( binomialCoef(n,k)) 