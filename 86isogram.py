p=list(input())
q=[]
for i in p:
    if i not in q:
        q.append(i)
if(p==q):
    print("Yes")
else:
    print("No")
