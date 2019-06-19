from itertools import permutations
p=input()
q=permutations(p)
for j in list(q):
    print("".join(j))
