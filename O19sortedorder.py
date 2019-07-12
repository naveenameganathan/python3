p=int(input())
q=[]
while(p):
    q+=list(map(int,input().split()))
    p-=1 
q=sorted(q)
print(*q)
