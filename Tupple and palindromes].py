def palind(r):
    e = len(r) -1
    S= 0  
    while(S<e):
        if(r[S!=r[e]]):
            return False
        S+=1
        e -= 1
    return True
r = (1,2,3,3,2,1)
if palind(r):
    print("Tuple is palindrome")
else:
    print("Tuplle is not a palindrome")
    