def mergeSortedAray(array1,array2):
   
    #resultant array
    mergedArray=[]
   
    i=0#iterate over array1 elements
    j=0#iterate over array2 elements
    
    
    #merging the two sorted array
    while i<len(array1) and j<len(array2):
       
       #since we have to maintain the intial ordering of the elements
       #if both the array elements are same then we will maintain the intial ordering
        if array1[i]<=array2[j]:
            mergedArray.append(array1[i])
            i+=1
        #if array2 element is less than array1 element
        else:
            mergedArray.append(array2[j])
            j+=1
    #in such cases where array1 have remaining elements
    while i<len(array1):
        mergedArray.append(array1[i])
        i+=1
    #in such cases where array2 have remaining elements
    while j<len(array2):
        mergedArray.append(array2[j])
        j+=1
    #returning tha merged array
    return mergedArray

array1=[1,2,3,4,5,6,7]
array2=[1,1,2,3]
#function call
print(mergeSortedAray(array1,array2))   

    