p,q=map(int,input().split())
n=0
Lst=[]
for i in range(p):
      Lst.append(input())
for j in range(p):
      for p in range(q-1):
            if(Lst[j][p]!='R' and Lst[j][p+1]!='R'):
                  n=n+3
            elif(Lst[j][p]!='G' and Lst[j][p+1]!='G'):
                  n=n+5
print(n)
