p,q=map(int,input().split())
for j in range(1,100000):
    if(j%p==0 and j%q==0):
        print(j)
        break
