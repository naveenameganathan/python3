A6,B6,C6=map(int,input().split())
num=0
for i in range(0,C6):
    num=num+A6
    A6=A6+B6
print(num)
