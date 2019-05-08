# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input())
x = [int(x) for x in input().strip().split(' ')]
x=set(x)
l=len(x)
if l==1:
    print(0)
else:    
    so=sorted(x, reverse=True)
    print(so)
    print(so[1])
    