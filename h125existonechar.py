p=input()
for i in range(len(p)):
    if(p.count(p[i])==1):
        print(p[i],end="")
