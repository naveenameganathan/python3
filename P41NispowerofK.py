N=int(input())
k=int(input())

if N <= 0 or k <=0:
    print ("not a valid input")
else:
    for i in range (1,200):
        x = k**i
        if x == N :
            print ("yes")
            break
        elif x> N:
            print ("no")
            break
