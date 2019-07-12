p,q=map(int,input().split())
m=max(p,q)
while(1):
   if(m%p==0 and m%q==0):
          print(m)
          break
   m+=1
