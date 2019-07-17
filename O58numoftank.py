p = int(input())
q = []
d = p//2 + p
for i in range(1,p+1):
  if i%2==0:
    q.append(i)
for i in range(1,p+1):
  if i%2!=0:
    q.append(i)
for i in range(1,p+1):
  if i%2==0:
    q.append(i)
print(d)
print(*q)
