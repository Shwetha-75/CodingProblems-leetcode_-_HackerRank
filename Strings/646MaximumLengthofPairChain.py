class Solution:
      def findLongestChain(self, pairs: list[list[int]]) -> int:
          pairs.sort(key=lambda x:x[1])
          result=[pairs[0]]
          for pair in pairs:
              if result[-1][1]<pair[0]:
                  result.append(pair[:])              
          return len(result)
class TestApp:
      def testing_case_one(self):
          assert Solution().findLongestChain([[1,2],[2,3],[3,4]])==2 
      def testing_case_two(self):
          assert Solution().findLongestChain([[1,2],[7,8],[4,5]])==3