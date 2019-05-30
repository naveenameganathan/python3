num=int(input())
p=list(map(int,input().split()))
q=sorted(p)
for i in range(0,len(p)):
    if(q[i]!=p[i]):
        print(i)
        break
