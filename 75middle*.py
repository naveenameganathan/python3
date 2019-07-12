p = input()
q = len(p)
r = q//2
if q%2 == 1 :
    s = p[:r] + '*' + p[r+1:]
else :
    s = p[:r-1] + '**' + p[r+1:]
print(s)
