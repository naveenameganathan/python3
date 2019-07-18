p=input()
q= 0
for i in range(0,len(p)-1):
  for j in range(i+1,len(p)):
    l=p[i:j+1]
    if l==l[::-1]:
      if len(l) > q:
        q = len(l)
        k=l
print(k)
