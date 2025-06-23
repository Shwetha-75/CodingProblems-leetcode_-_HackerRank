class Solution:
      def fibonacciSeries(self,number:int):
          if number<=1:
             return number
          return self.fibonacciSeries(number-1)+self.fibonacciSeries(number-2)
class Solution:
      def fibonacciSeries(self,number:int):
          dp=[0]*(number+1)
          dp[1]=1 
          for i in range(2,number+1):
              dp[i]=dp[i-1]+dp[i-2]
          return dp[-1]
class TestApp:
        def testing_case_one(self):
            assert Solution().fibonacciSeries(5)==5 
        def testing_case_two(self):
            assert Solution().fibonacciSeries(3)==2
