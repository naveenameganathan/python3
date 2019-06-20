p=int(input())
q=list(map(int,input().split()))
r=[]
while(len(q)!=0):
   if len(q)>1: 
        r.append(max(q))
        r.append(min(q))
        q.remove(max(q))
        q.remove(min(q))
   else:
       r.append(max(a))
       q.remove(max(a))
for i in r:
     print(i,end=" ")   
