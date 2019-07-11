p=int(input())
q=list(map(int,input().split()))
c=1
for i in range(0,p-2,2):
    if q[i]<q[i+1] and q[i+1]>q[i+2]:
        c=c+2
    elif q[i]>q[i+1] and q[i+1]<q[i+2]:
        c=c+2
    else:
        break
if c==p:
    print("yes")
else:
    print("no")
