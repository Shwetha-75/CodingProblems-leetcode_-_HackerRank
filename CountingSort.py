def countingSort(array):
    list1=[0]*10
    #counting the frequencies
    for i in array:
        list1[i]+=1
    # 0 1 2 3 4 5 6 7 8 9
    #[0,2,3,2,1,0,1,0,1,0]
    #finding cummulative sum
    for i in range(1,len(list1)):
        list1[i]=list1[i-1]+list1[i]
    #[0,2,3,2,1,0,1,0,1,0]  (0-9)
    # |/|/|/|/|/|/|/|/|/|+
    #[0,2,5,7,8,8,9,9,10,10]
    #
    #find the resultant array
    result=[0]*len(array)
    #0 --> 4 -1 -->3 at result[3]=0
    for i in reversed(array):
        #taking the value of cummulative sum 
        #subtracting it by 1 and updating it at the list1 value
        list1[i]=list1[i]-1
        #placing the element at correct position in sorted order
        result[list1[i]]=i
    # 0 1 2 3 4 5 6 7 8 9 
    #[0,2,5,7,8,8,9,9,10,10]
    #   1 4 6 7   8         --->-1
    #   0 3 5               --->-1
    #     2                 --->-1
    #[4,1,2,3,6,8,1,2,2,3]
    #                 <---
    # 0 1 2 3 4 5 6 7 8 9
    #[1,1,2,2,2,3,3,4,6,8]
    print(result)
    
    
countingSort([4,1,2,3,6,8,1,2,2,3])