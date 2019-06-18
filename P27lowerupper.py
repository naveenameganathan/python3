p=input()
for j in p:
    if j.isupper():
        print(j.lower(),end='')
    elif j.islower():
        print(j.upper(),end='')
