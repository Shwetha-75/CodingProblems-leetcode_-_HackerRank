list1=[]
#function for permutation
def permutation(array,i):
    #pushing the array element on to the list
    if i==len(array)-1:
        list1.append(array[::])
    #traversing through array elements
    for j in range(i,len(array)):
        #swapping
        array[i],array[j]=array[j],array[i]
        #function call recursively
        permutation(array,i+1)
        #swapping
        array[i],array[j]=array[j],array[i]
    #returning the list at the end
    return list1
array=[1,2,3]
i=0
print(permutation(array,i))