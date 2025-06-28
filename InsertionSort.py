def insertionsorting(array):
    n=len(array)
    #outer loop
    for i in range(1,n):
        #intializing the variable
        j=i-1
        temp=array[i]
        #condition
        while j>=0 and array[j]>temp:
            #push 
            array[j+1]=array[j]
            j-=1
        array[j+1]=temp
    return array


array=[2,6,0,8,5,6]
print(insertionsorting(array))        