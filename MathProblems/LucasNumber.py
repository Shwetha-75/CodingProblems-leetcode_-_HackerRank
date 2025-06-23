class Solution:
        def findLucasNumber(self,n:int):
            def helper(number:int):
                if number==0:
                    return 2 
                if number==1:
                    return 1 
                return helper(number-1)+helper(number-2)
            return helper(n)
class Solution:
      def findLucasNumber(self,n:int):
          if n==0: return 2 
          if n==1: return 1
          dp=[0]*(n+1)
          dp[0]=2 
          dp[1]=1
          for i in range(2,n+1):
              dp[i]=dp[i-1]+dp[i-2]
          return dp[-1]
class TestApp:
      def testing_case_one(self):
          assert Solution().findLucasNumber(2)==3 
      def testing_case_two(self):
          assert Solution().findLucasNumber(0)==2 
      def testing_case_three(self):
          assert Solution().findLucasNumber(9)==76