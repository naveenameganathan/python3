p=int(input())
q=input().split(' ')
r= [int(j) for j in q]
r.sort()
for j in range (p):
    print(r[j],end=" ")
