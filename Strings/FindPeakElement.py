class Solution:
      def findPeakElement(self, nums: list[int]) -> int:
          max_element=float('-inf')
          index=-1
          for i in range(len(nums)):
              if max_element<nums[i]:
                  max_element=nums[i]
                  index=i
          return index
class Solution:
      def findPeakElement(self, nums: list[int]) -> int:
          left=0
          right=len(nums)-1
          while left<right:
                mid=(left+right)//2 
                if nums[mid]>nums[mid+1]:
                    right=mid 
                else:
                    left=mid+1 
          return left
class TestApp:
      def testing_case_one(self):
          assert Solution().findPeakElement([1,2,3,1])==2 
      def testing_case_two(self):
          assert Solution().findPeakElement([1,2,1,3,5,6,4])==5