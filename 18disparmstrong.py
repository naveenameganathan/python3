a=int(input())
b=int(input())
for num in range(a,b):
    c=num
    sum=0
    while(c>0):
       digit=c%10
       sum+=digit**3
       c=c//10
       if(sum==num):
           print(num)
