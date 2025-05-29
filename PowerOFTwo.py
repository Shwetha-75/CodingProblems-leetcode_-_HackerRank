'''
19-02-2024 day problem

To check wherther the given number is power of 2^x

'''
import math
def power(n):
    
    if n==1: return True 
    '''
    
    for n=6 bot will return differnet value
    res1=2, res2=3
    n=16
    res=4, res2=4
    #Approach 1 
    #will pass only 1108 test cases
    res1=math.floor(math.log(n)/math.log(2))
    res2=math.ceil(math.log(n)/math.log(2))
    print(res1,res2)'''
    
    
    #Approach 2
    #we have to take bitwise & of n and n-1
    
    #n=6                 n=4
    # 110                100
    # 101                011
    # 100--> not 5       000-->0 
    
    return n>0 and (n & (n-1))==0
n=16
print(power(n))
        
    