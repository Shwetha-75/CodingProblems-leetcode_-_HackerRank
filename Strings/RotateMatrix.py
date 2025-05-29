class Solution:
        def rotateMatrix(self, matrix:list[list[int]])->list[list[int]]:
            row=len(matrix)
            col=len(matrix[0])
            dup_matrix=[[0]*col for _ in range(row)]
           
            for i in range(row):
                for j in range(col):
                    dup_matrix[i][j]=matrix[i][j]
            for i in range(col):
                for j in range(row):
                    matrix[i][j]=dup_matrix[j][i]
                   
            for arr in matrix:
                start,end=0,col-1
                while start<=end:
                      arr[start],arr[end]=arr[end],arr[start]
                      start+=1
                      end-=1 
class Solution:
      def rotateMatrix(self,matrix:list[list[int]])->None:   
          n=len(matrix)
          for i in range(n//2):
            for j in range(i,n-i-1):
                  top_left=matrix[j][i]
                  matrix[j][i]=matrix[n-i-1][j]
                  matrix[n-i-1][j]=matrix[n-j-1][n-i-1]
                  matrix[n-j-1][n-i-1]=matrix[i][n-j-1]
                  matrix[i][n-j-1]=top_left 
                 
          
class TestApp:
      def testing_case_one(self):
          matrix=[[1,2,3],[4,5,6],[7,8,9]]
          Solution().rotateMatrix(matrix)
          print(matrix)
          assert matrix==[[7,4,1],[8,5,2],[9,6,3]]
      def testing_case_two(self):
          matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
          Solution().rotateMatrix(matrix)
          print(matrix)
          assert matrix==[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
      def testing_case_three(self):
          matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
          Solution().rotateMatrix(matrix)
          assert matrix==[[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]]