def mergeSort(array1,array2):
    #resultant array
    mergeArray=[]
    i=0#iterate over array1 elements
    j=0#itertae over array2 elements
    
    #merging two arrays
    while i<len(array1) and j<len(array2):
        #condition to appaend the elements in sorted order 
        #as well as to even maintain the intial ordering of the array elements
        if array1[i]<=array2[j]:
            mergeArray.append(array1[i])
            i+=1
        else:
            mergeArray.append(array2[j])
            j+=1
    #such cases len(array1)>len(array2)
    #append the remaining elements of array1
    while i<len(array1):
        mergeArray.append(array1[i])
        i+=1
        
    #such cases len(array2)>len(array1)
    #append the remaining elements of array2
    while j<len(array2):
        mergeArray.append(array2[j])
        j+=1
    
    
    return mergeArray
    
#dividing the into two halves
def divide(array):
    if len(array)<=1:
        return array[::]
    #calculating mid value
    middle=len(array)//2
    #recursive acll at left side
    leftside=divide(array[:middle:])
    #recursive call at right side
    rightside=divide(array[middle::])
    return mergeSort(leftside,rightside)

array1=[6,5,1,2,4]
print(divide(array1))