class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count=0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                   self.dfs(grid,i,j)
                   count+=1 
        return count
 
    def dfs(self,grid:list[list[int]],i:int,j:int):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return 
        grid[i][j]='#'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)

class TestApp:
      def testing_case_one(self):
          assert Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])==1 
      def testing_case_two(self):
          assert Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])==3