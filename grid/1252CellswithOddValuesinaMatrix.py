class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]=[[0]]) -> int:
        matrix=[[0]*n for _ in range(m)]
        for index in indices:
            # incrementing the rows and keeping columns constant 
            for i in range(m):
                matrix[i][index[1]]+=1
            for i in range(n):
                matrix[index[0]][i]+=1
        # count odds 
        count=0 
        for i  in range(m):
            for j in range(n):
                if matrix[i][j]%2: count+=1
        return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().oddCells(2,3,[[0,1],[1,1]])==6 
      def testing_case_two(self):
          assert Solution().oddCells(2,2,[[1,1],[0,0]])==0