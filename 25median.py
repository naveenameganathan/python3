n=int(input())
p=input().split(' ')
q= [int(i) for i in p]
q.sort()
n=int(n/2)
print(q[n])
