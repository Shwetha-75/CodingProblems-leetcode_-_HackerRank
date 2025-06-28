class Sort:
    def sortedSquareArray(array):
        #creating the new Array
        newArray=[]
        #traversing through array
        for i in array:
            #squaring the array elements
            newArray.append(i*i)
        #sorting the array elements
        newArray.sort()
        #returning the array elements
        return newArray
array=[-3,-1,0,1,2]  
newArray=Sort.sortedSquareArray(array)
print(newArray)