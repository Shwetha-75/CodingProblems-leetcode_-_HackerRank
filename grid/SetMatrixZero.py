from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        hash_row,hash_col=defaultdict(int),defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0: 
                   hash_row[i]+=1 
                   hash_col[j]+=1 
        for i in range(len(matrix)):
            if i in hash_row:
               matrix[i]=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in hash_col:
                    matrix[i][j]=0
                
        
class TestApp:
      def testing_case_one(self):
          matrix=[[1,1,1],[1,0,1],[1,1,1]]
          Solution().setZeroes(matrix) 
          assert matrix==[[1,0,1],[0,0,0],[1,0,1]]
      def testing_case_two(self):
          matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
          Solution().setZeroes(matrix)
          assert matrix==[[0,0,0,0],[0,4,5,0],[0,3,1,0]]