p=str(input())
l=[]
t=""
r=0
for i in range(0,len(p)):
    for j in range(i,len(p)):
        t=t+p[j]
        if(t[::-1]==t):
            r=len(p)-len(t)
            l.append(r)
    t=""
print(min(l))
