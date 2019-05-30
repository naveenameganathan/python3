p,q,r=map(str,input().split())
s=int(p)
t=int(r)
if(q=="%"):
    print(int(s%t))
if(q=="/"):
    print(int(s/t))
