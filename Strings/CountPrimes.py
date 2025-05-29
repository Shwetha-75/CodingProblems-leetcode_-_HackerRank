class Solution:
     def countPrimes(self, n: int) -> int:
        count=0 
        if n==0: return 0
        if n==2: return 1 
        if n==3: return 2
        def helper(number:int):
             if number==0: return False 
             if number==1: return False  
             if number==2: return True  
             if number==3: return True 
             count=0
             for i in range(2,number):
                 if not number%i:
                     count+=1
                 if count>0:
                    return False 
             return count==0 
        for i in range(n):
            if helper(i):
                count+=1 
        return count 