n=int(input())
f=1
if n<0:
    print("Factorial does not have negative numbers")
elif n==0:
    print("1")
else:
    for i in range(1,n+1):
        f=f*i
    print(f)
