import sys
class Solution:
      def threeSumClosest(self, nums: list[int], target: int) -> int:
          sum_value=float('inf')
          result=0
          for i in range(len(nums)-2):
              for j in range(i+1,len(nums)-1):
                  for k in range(j+1,len(nums)):
                      temp=nums[i]+nums[j]+nums[k]
                      diff=abs(temp-target)
                      if diff<sum_value:
                          sum_value=diff
                          result=temp 
          return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().threeSumClosest([-1,2,1,-4],1)==2 
      def testing_case_two(self):
          assert Solution().threeSumClosest([0,0,0],1)==0
      def testing_case_three(self):
          assert Solution().threeSumClosest([1,1,1,0],-100)==2
      def testing_case_four(self):
          assert Solution().threeSumClosest([10,20,30,40,50,60,70,80,90],1)==60