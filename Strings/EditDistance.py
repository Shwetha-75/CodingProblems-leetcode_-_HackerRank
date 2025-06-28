# this exceeds h time  limit    

class Solution:
      def findMinimumNumberOfOperations(self,word1:str,word2:str)->int: 
          return self.operations(len(word1),len(word2),word1,word2)
      def operations(self,m:int,n:int,word1:str,word2:str):
          if m==0:
              return n
          if n==0:
              return m
          if word1[m-1] == word2[n-1]:
              return self.operations(m-1,n-1,word1,word2)
          return 1+min(
              
               self.operations(m-1,n,word1,word2),
                           self.operations(m,n-1,word1,word2),
               self.operations(m-1,n-1,word1,word2)
          )
          
# Optimal Approach   
class Solution:
      def findMinimumNumberOfOperations(self,word1:str,word2:str)->int: 
            row,col=len(word2),len(word1)
            dp=[[0]*(col+1) for _ in range(row+1)]
            dp[0]=[i for i in range(col+1)]
            for i in range(row+1):
                dp[i][0]+=i
            for i in range(1,row+1):
                for j in range(1,col+1):
                    if word1[j-1]!=word2[i-1]:
                       dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    else:
                        dp[i][j]=dp[i-1][j-1]
            return dp[-1][-1]
 
class TestApp:
      def testing_case_one(self):
          assert Solution().findMinimumNumberOfOperations("pale","bale")==1 
      def testing_case_two(self):
          assert Solution().findMinimumNumberOfOperations("intention","execution")==5 
      def testing_case_three(self):
          assert Solution().findMinimumNumberOfOperations("horse","ros")==3
          
          