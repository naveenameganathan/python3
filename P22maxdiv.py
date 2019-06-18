p,q=(map(int,input().split()))
r=min(p,q)
listval=list()
for j in range(1,r+1):
    if p%j==0 and q%j==0:
        listval.append(j)
print(max(listval))  
