def sortArrayByParity(nums):
    #Approach 1
    #To replace array elements 
    #By certain conditions
    #if nums[i] is odd then  i is odd 
    #if nums[i] is even then i is even
    ptr1=0#even indices
    ptr2=1#odd indices
    
    result=[0]*len(nums)
    #traversing through array elements
    for i in nums:
        #if the elements is even then replace at even index by even element
        if i%2==0:
            result[ptr1]=i
            ptr1+=2#increment it by 2 
        else:
            #odd element should be placed at odd indices
            result[ptr2]=i
            ptr2+=2
    #return the result
    return result 
nums=[4,2,5,7]
result=sortArrayByParity(nums)
print(result)