#Approach 1
li=[1,2,2,2,2,2,2,1,1]
li.sort()
print(li[len(li)//2])

#Approach 2
def maximumSort(array):
    #to store the value
    value=0
    #to store the maximum count
    count=0
    set1=set({})
    #traversing through array
    for i in array:
        #counting each element
        temp=array.count(i)
        #to exclude repeating element
        if i not in set1:
            #compare the previous count with current count
            if count<temp:
                #updating
                count=temp
                
                value=i
                set1.add(i)
    return value
array=[1,1,1,1,2,2,2]
print(maximumSort(array))