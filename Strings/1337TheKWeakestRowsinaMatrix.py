from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        for i in range(len(mat)):
            mat[i]=mat[i].count(1)
        hash_map=defaultdict(int)
        for i in range(len(mat)):
            hash_map[i]=mat[i]
        result=sorted(hash_map.items(),key=lambda x:x[1])
       
        for i in range(len(result)):
            result[i]=result[i][0]
      
        return result[:k:]
class TestApp:
      def testing_case_one(self):
          assert Solution().kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3)==[2,0,3]
          
      def testing_case_two(self):
          assert Solution().kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],2)==[0,2]

        