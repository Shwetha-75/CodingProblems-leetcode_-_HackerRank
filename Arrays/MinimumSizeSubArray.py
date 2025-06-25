import sys
class Solution:
      def minSubArrayLen(self, target: int, nums: list[int]) -> int:
          size=sys.maxsize 
          n=len(nums)
          for i in range(n):
              temp=0
              for j in range(i,n):
                  temp+=nums[j]
                  if temp>=target:
                     size=min(size,j-i+1)
          return size if size!=sys.maxsize else 0
class Solution:
      def minSubArrayLen(self, target: int, nums: list[int]) -> int:
          left=right=0
          min_size=sys.maxsize 
          total=0
          while left<len(nums) and right<len(nums):
                total+=nums[right]
                if total>=target:
                   min_size=min(min_size,right-left+1)
                   while left<=right and total>=target:
                         min_size=min(min_size,right-left+1)
                         total-=nums[left]
                         left+=1
                right+=1
          return min_size if min_size!=sys.maxsize else 0
class TestApp: 
      def testing_case_one(self):
          assert Solution().minSubArrayLen(7,[2,3,1,2,4,3])==2
      def testing_case_two(self):
          assert Solution().minSubArrayLen(11,[1,1,1,1,1,1,1,1])==0
      def testing_case_three(self):
          assert Solution().minSubArrayLen(4,[1,4,4])==1 
                     