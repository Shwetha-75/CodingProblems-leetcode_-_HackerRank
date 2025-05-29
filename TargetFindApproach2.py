def indicesTarget(array,target):
    #//creating map
    dict1={}
    #//dynamic array
    list1=[]
    #//traversing through array elements
    for i in range(len(array)):
        #calculatimg 
        temp=target-array[i]
        #checking whether the required elements suppose
        #target --> 7 array[i]-->4 suntracting both we get 3 if 3 is present in dict1 as key then
        #we can get the index of 3 as for key-value we stored like element-index
        if temp in dict1:
            list1.append(dict1.get(temp))
            list1.append(i)
            return list1
        else:
            #//if it is not present means we will be storing the in dict1
            dict1[array[i]]=i
    return list1
array=[5,4,3,2]
target=7
print(indicesTarget(array,target))    