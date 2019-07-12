p,q=map(int,input().split())
r=1
while(r<=p and r<=q):
    if(p%r==0 and q%r==0):
        ct=r
    r=r+1
print(ct)
