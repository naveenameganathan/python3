p=input()
a=0
b=0
for i in p:
    if i.isnumeric():
        a=1
    if i.isalpha():
        b=1
if(a==1 and b==1):
    print("Yes")
else:
    print("No") 
