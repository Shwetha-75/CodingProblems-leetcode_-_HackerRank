def permutation(array):    
    i=0
    list1=[]
    if len(array)==0:
        list1.append(array[::])
        return list1
    #function that performs recursion
    def funct(array,i):
        if i==len(array)-1:
            list1.append(array[::])#copying the array
        for j in range(i,len(array)):
            #swap
            array[i],array[j]=array[j],array[i]
            #recursion call
            funct(array,i+1)
            #swap
            array[i],array[j]=array[j],array[i]
    #calling the function
    funct(array,i)
    return list1
array=[1,2,3]
print(permutation(array))