class Solution:
      def findNumbers(self, nums: list[int]) -> int:
          count_even=0 
          for num in nums:
              if not len(str(num))%2: count_even+=1 
          return count_even 
class TestApp:
      def testing_case_one(self):
            assert Solution().findNumbers([12,345,2,6,7896])==2
      def testing_case_two(self):
            assert Solution().findNumbers([555,901,482,1771])==1