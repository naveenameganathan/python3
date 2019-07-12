p,q=map(int,input().split())
r=list(map(int,input().split()))
s=[]
for i in range(q):
    u,v=map(int,input().split())
    s.append(min(r[u-1:v]))
print(*s,sep="\n") 
