N= int(input())    
R = 0    
while(N > 0):    
    Re = N %10    
    R = (R *10) + Re    
    N = N //10    
     
print(R)
