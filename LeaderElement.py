def leader(array):
   #this approach passed 1009 test cases remaining 11 test should get passed :(
    #leader elements are such elements if it is greater than or equal to all the elements to ist right side    
    # 0 1 2 3 4 5 6  
    #[16,17,4,3,5,2]                         helper(0,6)  [16,17,4,3,5,2]             [16,17,4,3,5,2]    [16,17,4,3,5,2]       [16,17,4,3,5,2]     [16,17,4,3,5,2]     [16,17,4,3,5,2]             
    # i=0                                                   |          |                |        |         |      |             |     |              |  |                  ||
    #  left =0 right=6                                     left       right           left      right     left   right         left  right         left right           left right
    #    inde---> 1=helper(0)                                                 
    #  list1[17]
    # i=inde+1
    # i=2
    #
    #
    #
    #
    #
    ''' list1=[]
    def helper(left,right=len(array)-1):#helper function which will find the maximum among array elements
    #each time the array will be divided accordingly to the previous index value returned 
        while left<=right:
            if array[left]<array[right]:#if among them which is greater if 
            #smaller one encounters shifting the pointer of smaller element
                left+=1
            else:
                right-=1
        #at last returning the index of larger element
        return left
    i=0
    #iterating through array elements 
    while i<=len(array)-1:
    
        #the helper function will return the index of larger element
        index=helper(i)
        #appaending the larger element to the resultant list variable
       
        list1.append(array[index])
        #changing the ith variable value to point to next index (checking in next sub array)
        i=index+1
    print(list1)'''
    
    #this approach passed ......:)
    i=0
    list1=[]
    #simple approach 
    #here we are dividing the array into smaller sub array
    while len(array)!=0:
        #finding the max element among the given array
        num=max(array)
        #adding it to the list
        list1.append(num)
        #creating the subarray indexing starting from larger element index+1
        #storing it to the array(updating it)
        array=array[array.index(num)+1::]
    print(list1)
    
    
array=[1,2,3,4,0]

leader(array)   