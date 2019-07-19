p=int(input())
q=[]
for i in range(0,p):
   l=list(map(int,input().split()))
   q.append(l)
s=0
for i in range(0,p):
   for j in range(0,p):
      if i+j==p-1:
         s=s+q[i][j]
print(s)
