class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n==0 or target<0:
            return 1 if target==0 else 0 
        count=0 
        for i in range(1,k+1):
            count+=self.numRollsToTarget(n-1,k,target-i)
        return count%(10**9+7) 
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp=[[-1]*(target+1) for _ in range(n+1)]
        return self.helper(n,k,target,dp)
    def helper(self,n:int,k:int,target:int,dp:list[list[int]]):
        if n==0 or target<0:
            return 1 if target==0 else 0 
        if dp[n][target]!=-1:
            return dp[n][target]
        count=0 
        for i in range(1,k+1):
            count=(count+self.helper(n-1,k,target-i,dp))%(10**9+7)
        dp[n][target]=count 
        return dp[n][target]
class TestApp:
      def testing_case_one(self):
          assert Solution().numRollsToTarget(1,6,3)==1
      def testing_case_two(self):
          assert Solution().numRollsToTarget(2,6,7)==6 
      
        
        