# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:53:47 2019

@author: kingdurai
"""

m,n,k = input().split()
m=int(m)
n=int(n)
k=int(k)
print(m,n,k)
matrix=[[ -1 for i in range(n)] for j in range(m)]
matrix[2][2]=256
print(matrix[2][2])