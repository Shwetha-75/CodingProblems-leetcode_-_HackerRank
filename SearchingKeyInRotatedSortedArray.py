def searchingKey(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2#  7+6-->13/2-->6.5--.5--->6
        if array[mid]==target:
            return mid
        #checking left part is sorted 
        elif array[left]<=array[mid]:
            #checking target is rangeing between -->array[left]<=target<=array[mid]
            #if this is true we explore left part
            #i.e, changing the right pointer
            if target>=array[left] and target<=array[mid]:
                right=mid-1
            else:
                #if the target is not ranging between left or mid
                #we have to change the left pointer to have mid+1
                 left=mid+1
        else:#right part is sorted
            #checking if target is ranging between -->array[mid]<=target<=array[right]
            #if it true we have to explore the right part
            if target>=array[mid] and target<=array[right]:
                left=mid+1
            else:
                #if it is not in this range we have to explore left part
                right=mid-1
    return -1
array=[4,5,6,7,0,1,2]
target=1
print(searchingKey(array,target))