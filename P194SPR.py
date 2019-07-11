s,t=map(str,input().split())
if s==t:
    print("D")
elif (s=="R" and t=="P") or (s=="P" and t=="R"):
    print("P")
elif (s=="S" and t=="P") or (s=="P" and t=="S"):
    print("S")
elif (s=="S" and t=="R") or (s=="R" and t=="S"):
    print("R")
