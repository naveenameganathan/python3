p=int(input())
q=int(input())
for j in range(p,q+1):
    sum=0
    temp=j
    while(temp>0):
        digit=temp % 10
        sum += digit**3
        temp //= 10
    if j==sum:
        print(j)
