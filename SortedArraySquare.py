class Sort:
    def sortedArray(array):
        #defining the array of same size
        newArray=[0]*len(array)
        #left pointer
        left=0
        #right pointer
        right=len(array)-1
        #indexing the newArray
        k=len(array)-1
        #loop will work until the k==0
        #cause we inserting the array elemenet at index position
        while k>=0:
            #squaring the array elements
            num1=array[left]**2
            num2=array[right]**2
            if num1>num2:
                newArray[k]=num1
                #incrementing left pointer
                left+=1
                #decrementing indexes
                k-=1
            else:
                newArray[k]=num2
                #decrementing the array elements
                right-=1
                #decrementing the indexes
                k-=1
        return newArray
array=[-3,-1,0,1,2]
print(Sort.sortedArray(array))