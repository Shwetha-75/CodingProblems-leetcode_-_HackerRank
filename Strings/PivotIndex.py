class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        left=right=0
        for i in range(len(nums)):
            left=nums[i-1] if i>0 else 0
            if i>0:
                right=nums[-1]-nums[i-1]-(nums[i]-left)
            else:
                right=nums[-1]-nums[i]
            if left==right:
                return i 
        if nums[-1]==0: 
            return 0 
        
        return -1 
class TestApp:
      def testing_case_one(self):
          assert Solution().pivotIndex([1,7,3,6,5,6])==3 
      def testing_case_two(self):
          assert Solution().pivotIndex([1,2,3])==-1
      def testing_case_three(self):
          assert Solution().pivotIndex([2,1,-1])==0