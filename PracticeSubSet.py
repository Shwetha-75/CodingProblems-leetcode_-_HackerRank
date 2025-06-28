list1=[]
def subSetCreation(array):
    def helper(array,i,subset):
        if i==len(array):
            list1.append(subset[::])
            return
        helper(array,i+1,subset)
        subset.append(array[i])
        helper(array,i+1,subset)
        subset.pop()  
    i=0
    subset=[]
    helper(array,i,subset)
    return list1
array=[1,2,3]
print(subSetCreation(array))
    