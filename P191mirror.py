p=int(input())
q=list(map(int,input().split()))
r=list(map(int,input().split()))
if r[::-1]==q:
  print("yes")
else:
  print("no")  
