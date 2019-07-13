p = int(input())
q = list(map(int,input().split()))
c,l = 0,[]
b = [x for x in range(1,p+1)]
for i in q:
  if i in b:
    b.remove(i)
d = 0
for i in range(p-1):
  p = q[i]
  for j in range(i+1,p):
    if p == q[j]:
      if p < b[d]:
        q[j] = b[d]
        c += 1
      else:
        q[i] = b[d]
        c += 1
      d += 1
print(c)
print(*q)
