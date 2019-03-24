# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:48:27 2019

@author: Praison Joshua
"""
import math
testcase=int(input())
for i  in range(testcase):   
    
    n,k=[int(x) for x in input().split()]
    N=[]
    c=0
    
    

    N= list(map(int, input (). split ()))
        
    
    for i in range(n):
        sub=[]
        f=[0 for i in range(2001)]
        print('sub=',sub)
        print('f=',f)
        for j in range(i,n):
            
            start=0
            end=len(sub)
            print('end=',end)
            print('*****************')
            while (end-start) > 0:
                mid=int((start+end)/2)
                print('mid=',mid)
                
                if sub[mid]>N[j]:
                    end=mid
                    print('end=',end)
                else:
                    start=mid+1
                    print('start=',start)
            print('**************')        
                
            if (len(sub)>start and sub[start]<N[j]):
                start=start+1
                print('if:   start=',start)
            sub.insert(start,N[j])
            print('sub=',sub)
            f[N[j]]=f[N[j]]+1
            print('f=',f)
            l=(j-i)+1
            print('l=',l)
        
            m=math.ceil(k/l)
          
            print('m=',m)
            temp=int((k-1)/m)
            print('temp=',temp)
            x=sub[temp]
            print('x=',x)
            fv=f[x]
            print('fv=',fv)
            if(fv<2001 and f[fv] >0):
                c=c+1
                print('c=',c)
    print('Answer=',c)        
        