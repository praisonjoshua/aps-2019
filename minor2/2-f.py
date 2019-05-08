stringg="abcabc"
k='c'
lengg=len(stringg)
subsize= pow(2,lengg)
#if lengg<0 return case
c=0
cc=0
for i in range(subsize):
    for j in range(lengg):
        if(i & 1<<j):
            
            if stringg[j]==k:
                c=c+1
    
    
    if c>0:
        cc=cc+1

print(cc-1)