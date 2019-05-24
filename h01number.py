a=int(input())
listvalue=list(map(int(input().split())))
c=0
for i in listvalue:
    if listvalue.count(i)>1:
        print(i)
        break
else:
    print("unique")
