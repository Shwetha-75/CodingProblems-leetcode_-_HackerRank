import math
class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        if len(nums)<3:
            return 0 
        count=0 
        for i in range(1,len(nums)-1):
                if nums[i]==(nums[i-1]+nums[i+1])*2:
                   
                    count+=1 
        return count  
        
class TestApp:
      def testing_case_one(self):
          assert Solution().countSubarrays([1,2,1,4,1])==1 
      def testing_case_two(self):
          assert Solution().countSubarrays([1,1,1])==0 