import sys
class Solution:
      def findClosestNumber(self, nums: list[int]) -> int:
          n=len(nums)
          min_distance=sys.maxsize
          value=0
          for i in range(n):
              distance=abs(nums[i])
              if min_distance>=distance:
                 value=nums[i]
                 if min_distance==distance:
                     value=max(nums[i],value)
                 else:
                     value=nums[i]
                 min_distance=distance 
          return value 
class TestApp:
      def testing_case_one(self):
          assert Solution().findClosestNumber([-4,-2,1,4,8])==1
      def testing_case_two(self):
          assert Solution().findClosestNumber([2,-1,1])==1
      def testing_case_three(self):
          assert Solution().findClosestNumber([-100000,-100000])==-100000
          