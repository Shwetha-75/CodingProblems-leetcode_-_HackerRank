def frequentEvenCount(nums):
    #obersvations
    if len(nums)==0:
        return -1
    if len(nums)==1:
        if nums[0]%2==0:
            return nums[0]
        else:
            return -1
    
    #Approach 1
    '''list1=[] # to sort the evene elements in the list
    for i in nums:
        if i%2==0:
            list1.append(i)
    print(list1)'''
    #Approach 2
    #to get the evene elements
    #nums=list(filter(lambda i:i%2==0,nums))
    
    #Approach 3
    nums=[i for i in nums if i%2==0]
    
    if len(nums)==0:
        return -1
    
    #nums=sorted([i for i in nums if i%2==0])
    
    #nums.sort()
    
    #counting the frequncies
    dict1={}
    for i in nums:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    maxCountElement=0
    element=0
    for i in dict1:
        if maxCountElement<dict1[i]:
            maxCountElement=dict1[i]
            element=i
    return element
            
    
    
nums=[1,3,5,7,9]
print(frequentEvenCount(nums))