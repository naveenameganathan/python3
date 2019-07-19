p=input()
q=input()
r=[]
for i in range(0,len(p)):
    for j in range(0,len(q)):
        if p[i]==q[j] and j<=i:
            if p[i] not in r:
                r.append(p[i])
print(''.join(list(r)))
