p,q=map(int,input().split())
r=list(map(int,input().split()))
r.sort(reverse=True)
print(r[q-1])
