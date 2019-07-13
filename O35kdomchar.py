p=input()
l=list(set(p))
q=1
a=0
check=False
while True:
    ch=l[a]
    for j in range(0,len(p)-q):
        if ch in p[j:j+q]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l):
             a=0
             q+=1
            break

    if check==True:
        break
print(q)
