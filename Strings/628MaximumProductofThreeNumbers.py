class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        max_product=0 
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    max_product=max(max_product,nums[i]*nums[j]*nums[k])
        return max_product