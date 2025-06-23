class Solution:
      def maximumProduct(self, nums: list[int]) -> int:
          nums.sort()
          return max(nums[-3]*nums[-2]*nums[-1],nums[0]*nums[1]*nums[-1])
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumProduct([1,2,3])==6 
      def testing_case_two(self):
          assert Solution().maximumProduct([1,2,3,4])==24
      def testing_case_three(self):
          assert Solution().maximumProduct([-1,2,3,4,-100,-98])==39200