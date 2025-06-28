def powerOfThree(n):#not working
    
    if n==0: return 1
    return n>0 and (n  ^ (n-1))==1
n=21
print(powerOfThree(n))