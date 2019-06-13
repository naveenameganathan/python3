m,n=map(int,input().split())
o,p=map(int,input().split())
q,r=map(int,input().split())
if m==n or o==p or q==r:
    print("yes")
elif m==o==q or n==p==r:
    print("yes")
else:
    print("no")
