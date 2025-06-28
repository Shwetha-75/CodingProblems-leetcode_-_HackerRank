def missingNumber(nums):
    '''#Approach 1
    #creating aux array of size len(nums)+1
    aux=[0]*(len(nums)+1)
    #at indexs we will place 1 if it si present
    for i in nums:
        aux[i]=1
    #USE LSA
    for i in range(len(aux)):
        if aux[i]==0: return i'''
        
    #Approach 2
    n=len(nums)
    total_nums=n*(n+1)//2
    return total_nums-sum(nums)
    
   
    
    
print(missingNumber([0,1,2,3,4,5,6,8]))
    