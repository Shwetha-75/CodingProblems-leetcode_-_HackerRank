def arrange(nums):
    
    #observations 
    if len(nums)==0:
        return []
    if len(nums)==1:
        return nums
    array1=list(filter(lambda i:i<0,nums))#negative
    array2=list(filter(lambda i:i>0,nums))#positive
    result=[]
    #merging the two arrays
    i=0
    j=0
    while i<len(array1) and j<len(array2):
          result.append(array2[j])
          result.append(array1[i])
          i+=1
          j+=1
    print(result)
nums=[-1,1]
arrange(nums)
