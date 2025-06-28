class Solution:
      def findRotation(self, matrix: list[list[int]], target: list[list[int]]) -> bool:
            n=len(matrix)
            for _ in range(4):
                for i in range(n//2):
                    for j in range(i,n-i-1):
                        top_left=matrix[j][i]
                        matrix[j][i]=matrix[n-i-1][j]
                        matrix[n-i-1][j]=matrix[n-j-1][n-i-1]
                        matrix[n-j-1][n-i-1]=matrix[i][n-j-1]
                        matrix[i][n-j-1]=top_left 
                if matrix==target:
                    return True 
            return False 

class TestApp:
      def testing_case_one(self):
          assert Solution().findRotation([[0,1],[1,1]],[[0,1],[1,1]])==True 
      def testing_case_two(self):
          assert Solution().findRotation([[0,0,0],[0,1,0],[1,1,1]],[[1,1,1],[0,1,0],[0,0,0]])==True 
      def testing_case_three(self):
          assert Solution().findRotation([[0,1],[1,1]],[[1,0],[0,1]])==False 
      def testing_case_four(self):
          assert Solution().findRotation([[1,1],[0,1]],[[1,1],[1,0]])==True 