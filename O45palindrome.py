p=int(input())
while p%10==0:
  p=p//10
p=str(p)
re=p[::-1]
if p==re:
  print("yes")
else:
    print("no")
