def selectionSort(array):
    #outer loop
    n=len(array)
    for i in range(n):
        min=array[i]
        index=i
        for j in range(i+1,n):
            if array[j]<min:
                min=array[j]
                index=j
        #swapping
        array[i],array[index]=array[index],array[i]
    return array

array=[5,6,1,2,4]
print(selectionSort(array))