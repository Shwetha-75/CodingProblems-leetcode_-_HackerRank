# Recursive Approach 
class Solution:
      def maximumNumberOfSegments(self,n:int,x:int,y:int,z:int):
          return self.maxSegments(n,x,y,z)

      def maxSegments(self,n:int,x:int,y:int,z:int):
          if n==0: return 0 
          if n<0: return -1 
          return 1+max(self.maxSegments(n-x,x,y,z),self.maxSegments(n-y,x,y,z),self.maxSegments(n-z,x,y,z))
# Dynamic Programming 
class Solution:
      def maximumNumberOfSegments(self,n:int,x:int,y:int,z:int):
          dp=[0]*(n+1)
          for i in range(1,n+1):
              if i>=x and dp[i-x]!=-1:
                  dp[i]=max(dp[i],dp[i-x]+1)
              if i>=y and dp[i-y]!=-1:
                  dp[i]=max(dp[i],dp[i-y]+1)
              if i>=x  and dp[i-z]!=-1:
                  dp[i]=max(dp[i],dp[i-z]+1)
              if dp[i]==0:
                  dp[i]=-1
          return dp[n]

class TestApp:
      def testing_case_one(self):
          assert Solution().maximumNumberOfSegments(4,2,1,1)==4 
      def testing_case_two(self):
          assert Solution().maximumNumberOfSegments(5,5,3,2)==2
      def testing_case_three(self):
          assert Solution().maximumNumberOfSegments(10,1,3,2)==10