class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        count=0 
        for i in range(len(dominoes)):
            for j in range(i+1,len(dominoes)):
                if dominoes[i]==dominoes[j][::-1] or dominoes[i]==dominoes[j]:
                   count+=1 
        return count 
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        count=0 
        hash_map={}
        for domino in dominoes:
            print(hash_map)
            if str(domino[0])+str(domino[1]) in hash_map :
              count+=hash_map[str(domino[0])+str(domino[1])]
              hash_map[str(domino[0])+str(domino[1])]+=1
            elif str(domino[1])+str(domino[0]) in hash_map:
                count+=hash_map[str(domino[1])+str(domino[0])]
                hash_map[str(domino[1])+str(domino[0])]+=1
            else:
                hash_map[str(domino[0])+str(domino[1])]=1
        return count            
class TestApp:
      def testing_case_one(self):
          assert Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])==1 
      def testing_case_two(self):
          assert Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])==3 
    