p,q=input().split()
r=list(map(str,input().split()))
c=0
for j in range(0,len(r)):
    if(r[j]==q):
        c=c+1
print(c)
