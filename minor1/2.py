# # -*- coding: utf-8 -*-
# """
# Created on Sat Mar  2 22:46:45 2019

# @author: Praison Joshua
# """


# =============================================================================
# t=input()
# t=int(t)

# for i in range(t): 
# =============================================================================
# N,d=input().split()
# =============================================================================
# t=int(input())   
# for t in range(te):
#     N,d=input().split()
#     n=[int(i) for i in str(N)]
#     #print(n)
#     sum=str()
#     a=list()
#     u=len(n)
#     for i in range(u):
#         sum=sum+str(n[i])
#         a.append(sum+str(d*((u-1)-i)))
#     #print(n)
#     #print(a)
#     a.sort()   
#     print(a[0])
# =============================================================================
    
# t=int(input())   
# for t in range(te):
#     N,d=input().split()
#     n=[int(i) for i in str(N)]
#     n.append(int(d))
#     n.sort()
#     #print(n[:-1])   
#     new=list()
#     new=n[:-1]
#     for i in new: 
#         print(i, end="") 
def convert(list): 
    res = int("".join(map(str, list))) 
      
    return res 
def func(n,l):
    c=0
    for i in range(l-1):
        if n[(l-1)-i]<n[(l-1)-(i+1)]:
            n[(l-1)-(i+1)]=n[(l-1)-i]
            n[(l-1)-i]=n[l-1]
    for i in range(l-1):
        if n[(l-1)-i]<n[(l-1)-(i+1)]:
            func(n,l)
            c=c+1
    if c==0:
        print(convert(n[:-1]))      




te=int(input())   
for t in range(te):            
    N,d=input().split()
    n=[str(i) for i in str(N)]
    n.append(d)
    l=len(n)
    func(n,l)


  
    