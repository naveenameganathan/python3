n=int(input())
p=input().split(' ')
q= [int(j) for j in p]
q.sort()
for j in range (n):
    print(q[j],end=" ")
