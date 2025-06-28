def binarySearchAlgorithm(array,rows,columns,target):
    top=0
    bottom=rows
    mid=0
    left=0
    right=columns-1
    #finding the row matching
    #Few Observations 
    #1 if we have only one  element if the matrix(2D array)
    if len(array[0])==1:
        if target==array[0][0]:
            return True
        else:
            return False
    #2. if there is no elements 
    if len(array)==0:
        return False
    
    #3. if the target is greateer than minimum
    if target>array[rows-1][columns-1]:
        return False
    
    #finding the row to search the key
    while top<=bottom:
        #calculating the mid
        mid=(top+bottom)//2
        #if the target is less than array[mid][0] means in first index of the middle(mid) row
        if target<array[mid][0]:
            bottom=mid-1
        #if the target is greater than array[mid][columns-1] means in last index of the middle(mid) row
        elif target>array[mid][columns-1]:
            top=mid+1
        else:
            break
    
    
    #after finding the particular row 
    #fiding the elements in the wich row it is present
    #BSA applying of row where target is ranging
    while left<=right:
        #
        middle=(left+right)//2
        if target==array[mid][middle]:
            return True
        elif target>array[mid][middle]:
            left=middle+1
        else:
            right=middle-1
    return False
array=[[1,2,3],[4,5,6],[7,8,9]]
rows=3
columns=3
target=8

print(binarySearchAlgorithm(array,rows,columns,target))
