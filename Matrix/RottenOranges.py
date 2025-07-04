'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

'''

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        visited,queue={},[]
        # finding all the rotten oranges at 0 time
        row,col,count=len(grid),len(grid[0]),0 
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j,0))
                    visited[str(i)+str(j)]=1
        # checking for each item until all the cells are visited 
        print(queue )
        while queue:
              temp=queue.pop(0)
              print(temp)
              print(visited)
              print(queue)
              
              count=max(count,temp[2])
            #   up 
              if temp[0]-1!=-1 and str(temp[0]-1)+str(temp[1]) not in visited:
                  if grid[temp[0]-1][temp[1]]!=0:
                     grid[temp[0]-1][temp[1]]=2 
                     queue.append((temp[0]-1,temp[1],temp[2]+1))
                  visited[str(temp[0]-1)+str(temp[1])]=1
            #   down 
              if temp[0]+1!=row and str(temp[0]+1)+str(temp[1]) not in visited:
                  if grid[temp[0]+1][temp[1]]!=0:
                     grid[temp[0]+1][temp[1]]=2
                     queue.append((temp[0]+1,temp[1],temp[2]+1))
                  visited[str(temp[0]+1)+str(temp[1])]=1
            #   right 
              if temp[1]-1!=-1 and str(temp[0])+str(temp[1]-1) not in visited:
                  if grid[temp[0]][temp[1]-1]!=0:
                      grid[temp[0]][temp[1]-1]=2 
                      queue.append((temp[0],temp[1]-1,temp[2]+1))
                  visited[str(temp[0])+str(temp[1]-1)]=1
            #   left 
              if temp[1]+1!=col and str(temp[0])+str(temp[1]+1) not in visited:
                  if grid[temp[0]][temp[1]+1]!=0:
                      grid[temp[0]][temp[1]+1]=2
                      queue.append((temp[0],temp[1]+1,temp[2]+1))
                  visited[str(temp[0])+str(temp[1]+1)]=1
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1 
        return count 
Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]])
    
class TestApp:
      def testing_case_one(self):
          assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])==-1
      def testing_case_two(self):
          assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])==4
      def testing_case_three(self):
          assert Solution().orangesRotting([[0]])==0
      def testing_case_four(self):
          assert Solution().orangesRotting([[0,1]])==-1
      def testing_case_five(self):
          assert Solution().orangesRotting([[0,2]])==0
      def testing_case_six(self):
          assert Solution().orangesRotting([[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]])==58
# Solution().orangesRotting()