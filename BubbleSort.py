def bubbleSorting(array):
    n=len(array)
    #rnage of i <=n-2
    for i in range(n-1):
        #rnage of j<=n-2
        for j in range(n-1):
            #swapping
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
array=[5,6,1,2,4]
print(bubbleSorting(array))
    