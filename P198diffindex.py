p=int(input())
q=list(map(int,input().split()))
r=sorted(q)
print(q.index(r[len(r)-1])-q.index(r[0]))
