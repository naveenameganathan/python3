p=input()
q=map(int,input().split())
r=[]
for i in q:
    s=bin(i)
    r.append(s)
fine=sorted(r)
fine.reverse()
for j in fine:
    print(int(j,2))
