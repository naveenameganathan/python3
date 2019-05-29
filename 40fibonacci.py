num=int(input(""))
p=0
q=1
for j in range(num):
    r=p+q
    p=q
    print(p,end=" ")
    q=r
