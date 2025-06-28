class Solution:
      def minimCostClimbingStairs(self,cost:list[int]):
          cost=cost+[0]
          for i in range(len(cost)-3,-1,-1):
              cost[i]=min(cost[i]+cost[i+1],cost[i]+cost[i+2])
          return min(cost[0],cost[1])
class TestApp:
      def testing_case_one(self):
          assert Solution().minimCostClimbingStairs([10,15,20])==15 
      def testing_case_two(self):
          assert Solution().minimCostClimbingStairs( [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])==6