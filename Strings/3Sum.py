class Solution:
      def threeSum(self, nums: list[int]) -> list[list[int]]:
          result=[]
          n=len(nums)
          for i in range(n-2):
              for j in range(i+1,n-1):
                  for k in range(j+1,n):
                      if nums[i]+nums[j]+nums[k]==0:
                         result.append([nums[i],nums[j],nums[k]])
                      
          return list(result) 
class TestApp:
      def testing_case_one(self):
          assert Solution().threeSum([-1,0,1,2,-1,-4])==[[-1,-1,2],[-1,0,1]]
      def testing_case_two(self):
          assert Solution().threeSum([0,1,1])==[]
      def testing_case_three(self):
          assert Solution().threeSum([0,0,0])==[[0,0,0]]