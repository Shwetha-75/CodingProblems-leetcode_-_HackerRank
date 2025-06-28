# Problem given an array elements, return the count of number of operations taken to swap at the places
# at 0th index 1 should be placed
# at last index len(nums) shuld be placed
# directly you cannot swap
#
# [2,1,4,3]--->                     Eg2:  [2,4,1,3]
# [1,2,4,3]-->1                           [2,1,4,3] --->1
# [1,2,3,4]-->2                           [1,2,4,3]--->2
#total 2 operations                       [1,2,3,4]-->3 total number of opeartions 3

#APPROACH 1
def semiOrderdPermutationApproach1(nums):
    if nums[0]==1 and nums[len(nums)-1]==len(nums):
        print(0)
        return
    #swaping function for 1
    def swap1(nums):
        ind=nums.index(1)
        nums[ind-1],nums[ind]=nums[ind],nums[ind-1]
    #swaping fucntion for len(nums)
    def swapLast(nums):
        ind=nums.index(len(nums))
        nums[ind+1],nums[ind]=nums[ind],nums[ind-1]
    count=0
    #calling the function recursively until swapped or condition is not satisfied
    #taking the count of each recursive call
    while True:
        #if the 1 is at 0th index break the loop
        if nums[0]==1: break
        swap1(nums)
        count+=1 
    while True:
        #if len(nums) is at last index break the loop
        if nums[len(nums)-1]==len(nums): break
        swapLast(nums)
        count+=1 
    print(count)

#APPROACH 2

def semiOrderedPermutationAproach2(nums):
    first=last=0
    if nums[0]==1 and nums[len(nums)-1]==len(nums): return 0
    
    #iterating thorugh array
    n=len(nums)
    for index,value in enumerate(nums):
        if value==1:
            first=index 
        if value==n:
            last=index 
  
    if first>last:
        return first+((n-1)-last)-1
    else:
        return first+((n-1)-last)
              


nums=[2,4,1,3]

semiOrderdPermutationApproach1(nums)
nums=[2,4,1,3]
print(semiOrderedPermutationAproach2(nums))