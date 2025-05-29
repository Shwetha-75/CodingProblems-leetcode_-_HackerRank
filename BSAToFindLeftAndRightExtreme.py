#program to find the left and right extreme end of the given target value
#[0,1,2,3,4,5,5,5,5,6,7]  target=5
#range[5,8] -->indexes of target range between 5 and 8
#function to find left extreme end
def leftExtreme(array,target):
    #left and right pointer
    left=0
    right=len(array)-1
    #stopping condition
    while left<=right:
        #mid value
        mid=(left+right)//2
        #to check whether target in the mid index
        if target==array[mid]:
            #if found we go through 3 cases
            #case :1 
            #since we are checking for left extreme
            #we chck whether the mid value reached left extreme of the array
            if mid==0:
                return mid#return 0
            #case 2 
            #if the the [0,1,2,3,4,5,5,5,5,6,7]
                        # 0 1 2 4 5 6 7 8 9 10 11
            elif array[mid-1]==target:#if prevoius element is nothing but array[mid-1] index
                #perform BSA again
                right=mid-1 
            else:#case 3 
                #we found the left extreme
                return mid
        #performing BSA to shifthe left and right pointer according to the condition
        elif target>array[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
array=[1,1,7,7,7,7,7,7,7,7]
target=1
print(leftExtreme(array,target))
#function to fing right extreme of the target
def rightExtreme(array,target):
    #left and right pointers
    left=0
    right=len(array)-1
    #stopping condition
    while left<=right:
        #calculationg mid value
        mid=(left+right)//2
        #if we found we are going to have 3 cases
        if array[mid]==target:
            #case 1 is if we have reached end of the array
            if mid==len(array)-1:
                return mid
            #case 2 checking next element is target
            #if it then again perform BSA
            elif array[mid+1]==target:left=mid+1
            else:
                #we have found right extreme
                 return mid
        #checking the condtions to shift the left and right pointers
        elif target>array[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
print(rightExtreme(array,target))
    