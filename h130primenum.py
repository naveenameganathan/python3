p=int(input())
q=0
for i in range(3,p):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i%10==3:
            q=q+i 
print(q)
