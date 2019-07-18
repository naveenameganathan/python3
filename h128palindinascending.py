p=input()
ll=[]
for i in range(0,len(p)):
    for j in range(i+2,len(p)+1):
        aa=p[i:j]
        if aa==aa[::-1]:
            ll.append(aa)
ll.sort()
for i in range(0,len(ll)):
    print(ll[i])
