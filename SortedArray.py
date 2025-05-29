class Sort:
    def sortedArray(array):
        newArray=[0]*len(array)
        left=0
        right=len(array)-1
        for i in reversed(range(len(array))):
            num1=array[left]**2
            num2=array[right]**2
            if num1>num2:
                newArray[i]=num1
                left+=1
            else:
                newArray[i]=num2
                right-=1
        return newArray
array=[-3,-1,0,1,2]
print(Sort.sortedArray(array))