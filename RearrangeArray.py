def arrangeArray(nums):
    #Left ptr to check the indexes
    #right to check element at right index
    left=right=0
    
    while right<len(nums):
        #checking if either
        #left is odd and element at right index is also odd 
        #left is evene and element at right index is also even
        #swap at left index element with right index element
        if left%2==nums[right]%2:
            #swapping
            nums[left],nums[right]=nums[right],nums[left]
            #increment left
            left+=1
        else:
            #increment right
            right+=1
    return nums
nums=[4,2,5,7]
result=arrangeArray(nums)
print(result) #[4, 5, 2, 7]
    