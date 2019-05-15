nunum1,num2,num3=input().split()
n1=int(num1)
n2=int(num2)
n3=int(num3)
if(num1>num2) and (num1>num3):
    print(num1)
elif(num2>num1) and (num2>num3):
    print(num2)
else:
    print(num3)
