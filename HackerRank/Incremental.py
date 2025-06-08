import heapq
from collections import defaultdict
class Solution:
      def incrementalGridOperations(self,strings:list[str])->int:
            cols=[-int(string[1]) for string in strings]
            rows=[-int(string[0]) for string in strings]
            heapq.heapify(cols)
            heapq.heapify(rows)
            row=abs(rows[0])
            col=abs(cols[0])
           
            matrix=[[0]*col for _ in range(row)]
            for string in strings:
                for i in range(int(string[0])):
                    for j in range(int(string[1])):
                        matrix[i][j]+=1
                    
           
            hash_map=defaultdict(int)
            for i in range(row):
                for j in range(col):
                    hash_map[matrix[i][j]]+=1
            matrix=list(hash_map.items())
            matrix.sort(reverse=True,key=lambda x:x[0])
            
            return matrix[0][1]
class TestApp:
      def testing_case_one(self):
          assert Solution().incrementalGridOperations(["13","42","14","15"])==2 
      def testing_case_two(self):
          assert Solution().incrementalGridOperations(["14","24","35","64","51"])==1
      def testing_case_three(self):
          assert Solution().incrementalGridOperations(["23","41","24"])==2
            