num=int(input())
listval=list(map(int,input().split()))
for j in listval:
    if listval.count(j)==1:
    #result
        print(j)
