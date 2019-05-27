a=str(input())
l=list(a)
for i in range(0,len(a)):
    q=a[i].lower()
    if(q=="a" or q=="e" or q=="i" or q=="o" or q=="u"):
        l.remove(q)
for i in reversed(l):
    print(i,end=" ")
