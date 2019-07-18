p,q=list(map(str,input().split()))
l=[]
for i in p:
    for j in q:
        if i==j:
            l.append(i)
print("".join(l))
