p,q=list(map(int,input().split()))
count=0 
for j in range(p,q+1):
    if j*j >= p and j*j <= q:
        count=count+1
print(count) 
