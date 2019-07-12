p=int(input())
q=list(map(int,input().split()))
r=[1]*p
for pa in range(p):
    if pa==0:
        if q[pa]>q[pa+1]:
            r[pa]=r[pa]+r[pa+1]
    elif pa>0:
        if q[pa]>q[pa-1]:
            r[pa]=r[pa]+r[pa-1]
print(sum(r))
