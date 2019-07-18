p = int(input())
a,val = 3,3
while p > 0:
    if a == 0:
        val*=2
        a = val
    if p==1:
        print(a)
        break
    p -= 1
    a -= 1
