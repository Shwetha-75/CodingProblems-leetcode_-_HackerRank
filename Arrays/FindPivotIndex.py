class Solution:
      def pivotIndex(self, nums: list[int]) -> int:
          for i in range(len(nums)):
              if i==0:
                  if sum(nums[i+1::])==0:
                      return 0 
              elif i==len(nums)-1:
                   if sum(nums[:i:])==0:
                      return 0 
              elif sum(nums[:i:])==sum(nums[i+1::]):
                   return i 
          return -1 
class Solution:
      def pivotIndex(self, nums: list[int]) -> int:
          total=sum(nums)
          left=0 
          for i in range(len(nums)):
              right=total-left-nums[i]
              if left==right:
                  return i 
              left+=nums[i]
          return -1

class TestApp:
      def testing_case_one(self):
          assert Solution().pivotIndex([1,7,3,6,5,6])==3 
      def testing_case_two(self):
          assert Solution().pivotIndex([1,2,3])==-1
      def testing_case_three(self):
          assert Solution().pivotIndex([2,-1,1])==0