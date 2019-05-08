
# =============================================================================
# s='abcabc'
# a=list(s[i:j+1] for i in range (len(s)) for j in range(i,len(s)))
# print(a)
# =============================================================================

# =============================================================================
# t=int(input())    
# for testcase in range(t):    
# n=int(input())
# =============================================================================
s,c=input().split()

cc=0
for i in range (len(s)): 
    for j in range(i,len(s)):
        ss=list(s[i:j+1])
        
        
        if c in ss:
            cc=cc+1
            print(ss)

print(cc)            
