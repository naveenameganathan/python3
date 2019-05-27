k=int(input())
t=0
while(k>0):
    dig=k%10
    t=t+dig*dig
    k=k//10
print(t)
