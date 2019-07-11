p=int(input())
q=list(map(int,input().split()))
if len(q)==p:
    r=max(q)
    s=min(q)
    t=r-s
print(t)
