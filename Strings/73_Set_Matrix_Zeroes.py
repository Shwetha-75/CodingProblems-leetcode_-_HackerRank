from collections import defaultdict
class Solution:
      def setZeroes(self, matrix: list[list[int]]) -> None:
            row=defaultdict(int)
            col=defaultdict(int) 
            r,c=len(matrix),len(matrix[0]) 
            for i in range(r):
                for j in range(c):
                    if matrix[i][j]==0:
                        print(i,j)
                        row[i]+=1 
                        col[j]+=1 
                        print(row,col)
            for i in range(r):
                for j in range(c):
                    if i in row or j in col:
                        matrix[i][j]=0
            
            print(matrix)
class TestApp:
      def testing_case_one(self):
          matrix=[[1,1,1],[1,0,1],[1,1,1]]
          Solution().setZeroes(matrix)
          assert matrix==[[1,0,1],[0,0,0],[1,0,1]] 
      def testing_case_two(self):
          matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
          Solution().setZeroes(matrix)
          assert matrix==[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
      def testing_case_three(self):
          matrix=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
          Solution().setZeroes(matrix)
          assert matrix==[[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]   