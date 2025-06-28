class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        single_digit=double_digit=0 
        for num in nums:
            if num>=10:
                double_digit+=num 
            else:
                single_digit+=num 
        return single_digit!=double_digit 
    
class TestApp:
      def testing_case_one(self):
          assert Solution().canAliceWin([1,2,3,4,10])==False 
      def testing_case_two(self):
          assert Solution().canAliceWin([1,2,3,4,5,14])==True 
      def testing_case_three(self):
          assert Solution().canAliceWin([5,5,5,25])==True 