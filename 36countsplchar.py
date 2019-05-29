p= input()
c = 0
for j in p:
    if( j.isalpha() or j.isnumeric()):
        y = 0
    else:
        c = c+1
print(c)
