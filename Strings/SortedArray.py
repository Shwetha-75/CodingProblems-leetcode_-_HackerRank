class Solution:
        def sortedSquares(self, nums: list[int]) -> list[int]:
            for i in range(len(nums)):
                nums[i]*=nums[i]
            left,right=0,len(nums)-1 
            while left<right:
                  if nums[left]>nums[right]:
                     nums[left],nums[right]=nums[right],nums[left]
                  right-=1 
            return nums 
class TestApp:
      def testing_case_one(self):
          assert Solution().sortedSquares([-4,-1,0,3,10])==[0,1,9,16,100]
      def testing_case_two(self):
          assert Solution().sortedSquares([-7,-3,2,3,11])==[4,9,9,49,121]