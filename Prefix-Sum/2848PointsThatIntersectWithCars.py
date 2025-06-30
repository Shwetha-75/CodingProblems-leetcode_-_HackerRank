from collections import defaultdict
class Solution:
      def maximumPopulation(self, logs: list[list[int]]) -> int:
          logs.sort(key=lambda x:x[0])
          n=len(logs)
          result=[logs[0]]
          for i in range(1,n):
              if result[-1][-1]>=logs[i][0]:
                  result[-1]=[result[-1][0],max(result[-1][1],logs[i][1])]
              else:
                  result.append(logs[i])
          count=0 
          for res in result:
               count+=res[1]-res[0]+1
          return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumPopulation([[3,6],[1,5],[4,7]])==7
      def testing_case_two(self):
          assert Solution().maximumPopulation([[1,3],[5,8]])==7                 
              