p=input()
q=[]
for i in p:
  if i not in q:
    q.append(i)
  else:
    break  
print(len(q))
