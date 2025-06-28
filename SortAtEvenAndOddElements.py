def sortArray(nums):
    array1=sorted(list(filter(lambda i:i%2==0,nums)))
    array2=sorted(list(filter(lambda i:i%2!=0,nums)),reverse=True)
    result=[]
    i=j=0
    while i<len(array1) and j<len(array2):
        result.append(array1[i])
        result.append(array2[j])
        i+=1
        j+=1
    print(result)
    print(array1)
    print(array2)
nums=[1,4,2,1,7,8]
sortArray(nums)