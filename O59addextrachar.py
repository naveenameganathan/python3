p=input()
b=input()
c=p.index('|')
d=len(p)+len(b)
if d%2==0:
    print("Impossible")
else:
    if c<=d//2-1:
        p=b+p
    else:
        p=p+b
    c=p.index('|')
    if c!=d//2-1 and c!=d//2:
        print("Impossible")
    else:
        print(p)
