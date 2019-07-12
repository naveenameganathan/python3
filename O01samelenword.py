p=int(input())
q=[]
for i in range(0,p):
  r=input()
  q.append(r)
s=[]
for i in zip(*q):
  if(i.count(i[0])==len(i)):
    s.append(i[0])
  else:
    break
print(''.join(s))   
