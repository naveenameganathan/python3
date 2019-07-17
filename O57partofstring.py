p,q=map(str,input().split())
count=0
for i in range(0,len(p)):
    for j in range(0,len(q)):
        if p[i]==q[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
