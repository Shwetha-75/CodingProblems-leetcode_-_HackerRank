# Wrong solution
class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        # sorting the queries based on farthest ending points
        queries=[[query[0],query[1],query[1]-query[0]] for query in queries]
        queries.sort(key= lambda x:x[2],reverse=True)
        diff=[0]*(len(nums)+1)
        while queries:
              query=queries.pop(0)
              diff[query[0]]+=1 
              diff[query[1]+1]-=1 
              flag=True
              temp=diff[::]
              for i in range(len(nums)):
                  temp[i]+=temp[i-1] if i>0 else 0 
                  if temp[i]<nums[i]:
                      flag=False 
                      break 
              if flag:
                  return len(queries)
        return -1
class TestApp:
      def testing_case_one(self):
          assert Solution().maxRemoval([2,0,2],[[0,2],[0,2],[1,1]])==1
      def testing_case_two(self):
          assert Solution().maxRemoval([1,1,1,1],[[1,3],[0,2],[1,3],[1,2]])==2 
      def testing_case_three(self):
          assert Solution().maxRemoval([1,2,3,4],[[0,3]])==-1
      def testing_case_four(self):
          assert Solution().maxRemoval([1,0],[[1,1],[1,1],[0,1],[0,1],[0,0],[1,1]])==5
      def testing_case_five(self):
          assert Solution().maxRemoval([0,3],[[0,1],[0,0],[0,1],[0,1],[0,0]])==2