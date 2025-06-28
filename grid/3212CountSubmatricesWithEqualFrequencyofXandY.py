class Solution:
      def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
            row=len(grid)
            col=len(grid[0])
            result=0
            x=[[0]*(col+1) for _ in range(row+1)]
            y=[[0]*(col+1) for _ in range(row+1)]
            for i in range(1,row+1):
                for j in range(1,col+1):
                    x[i][j]=x[i-1][j]+x[i][j-1]-x[i-1][j-1]+(grid[i-1][j-1]=='X')
                    y[i][j]=y[i-1][j]+y[i][j-1]-y[i-1][j-1]+(grid[i-1][j-1]=='Y')
                    if x[i][j]==y[i][j]>0:
                       result+=1
            return result
class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfSubmatrices([["X","Y","."],["Y",".","."]])==3 
      def testing_case_two(self):
          assert Solution().numberOfSubmatrices([["X","X"],["X","Y"]])==0 
      def testing_case_three(self):
          assert Solution().numberOfSubmatrices([[".","."],[".","."]])==0 
      def testing_case_four(self):
          assert Solution().numberOfSubmatrices([['X','X','.'],['Y','Y','.'],['X','X','.'],['Y','Y','.']])==6      
