def permutation(nums):
    pivot=-1
    for i in reversed(range(1,len(nums))):
        if nums[i-1]<nums[i]:
            pivot=i-1
            break
    print(pivot)
    if pivot!=-1:
        i=len(nums)-1
       
        while i<len(nums) and i>pivot:
          
            if nums[i]>nums[pivot-1]:
               nums[i],nums[pivot-1]=nums[pivot-1],nums[i]
               break 
            i-=1
        left=pivot+1
        right=len(nums)-1
        while left<=right:
            nums[left],nums[right]=nums[left],nums[right]
            left+=1
            right-=1
    else:
        nums=nums[::-1]
    print(nums)
    
nums=[2,4,3,1]
permutation(nums)