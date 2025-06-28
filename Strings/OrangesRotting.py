class Solution:
      def orangesRotting(self, grid: list[list[int]]) -> int:  
            minutes=0 
            row=len(grid)
            col=len(grid[0])
            for i in range(row):
                for j in range(col):
                    if grid[i][i]==2:
                      #  upper left corner
                    
                      if i==0 and j==0 and (grid[i][j+1]==1 or grid[i+1][j])==1:
                         grid[i][j+1]=2 if grid[i][j+1] ==1 else grid[i][j+1]
                         grid[i+1][j] =2 if grid[i+1][j] ==1 else grid[i+1][j] 
                         minutes+=1 
                      elif i==0 and j==col-1 and (grid[i][j-1]==1 or grid[i+1][j])==1:
                         grid[i][j-1] = 2 if grid[i][j-1]==1 else grid[i][j-1]
                         grid[i+1][j]= 2 if grid[i+1][j] ==1 else grid[i+1][j]
                         minutes+=1
                      elif i==row-1 and j==0 and (grid[i-1][j]==1 or grid[i][j+1])==1:
                         grid[i-1][j] = 2 if grid[i-1][j]==1 else grid[i-1][j]
                         grid[i][j+1] = 2 if grid[i][j+1] ==1 else grid[i][j+1] 
                         minutes+=1 
                      elif i==row-1 and j==col-1 and (grid[i-1][j]==1 or grid[i][j-1])==1:
                         grid[i-1][j] = 2 if grid[i-1][j]==1 else grid[i-1][j] 
                         grid[i][j-1] = 2 if grid[i][j-1]==1 else grid[i][j-1] 
                         minutes+=1
                      elif i==0 and j<col-1 and (grid[i+1][j]==1 or grid[i][j-1]==1 or grid[i][j+1])==1:
                           grid[i+1][j] = 2 if grid[i+1][j] ==1 else grid[i+1][j] 
                           grid[i][j-1] = 2 if grid[i][j-1] ==1 else grid[i][j-1]
                           grid[i][j+1]= 2 if grid[i][j+1]==1 else grid[i][j+1]
                           minutes+=1 
                      elif j==0 and i<row-1 and (grid[i-1][j]==1 or grid[i][j+1]==1 or grid[i+1][j])==1:
                           grid[i-1][j] = 2 if grid[i-1][j] ==1 else grid[i-1][j] 
                           grid[i][j+1] = 2 if grid[i][j+1] ==1 else grid[i][j+1]  
                           grid[i+1][j] = 2 if grid[i+1][j] ==1 else grid[i+1][j]
                           minutes+=1 
                      elif i==row-1 and j<col-1 and (grid[i][j-1]==1 or grid[i-1][j]==1 or grid[i][j+1])==1:
                           grid[i][j-1]=2 if grid[i][j-1]==1 else grid[i][j-1] 
                           grid[i-1][j]=2 if grid[i-1][j]==1 else grid[i-1][j]
                           grid[i][j+1]=2 if grid[i][j+1]==1 else grid[i][j+1] 
                           minutes+=1
                      elif j==col-1 and i<row-1 and (grid[i][j-1]==1 or grid[i-1][j]==1 or grid[i+1][j])==1:
                           grid[i][j-1] = 2 if grid[i][j-1]==1 else grid[i][j-1] 
                           grid[i-1][j] =2 if grid[i-1][j]==1 else grid[i-1][j] 
                           grid[i+1][j] =2 if grid[i+1][j]==1 else grid[i+1][j] 
                           minutes+=1 
                      elif i>0 and j>0 and j<col-1 and i<row-1 and (grid[i-1][j-1]==1 or grid[i][j-1]==1 or grid[i][j+1]==1 or grid[i+1][j]==1):
                           grid[i-1][j-1] = 2 if grid[i-1][j-1]==1 else grid[i-1][j-1]
                           grid[i][j-1]=2 if grid[i][j-1]==1 else grid[i][j-1]
                           grid[i][j+1] =2 if grid[i][j+1] ==1 else grid[i][j+1]
                           grid[i+1][j] =2 if grid[i+1][j]==1 else grid[i+1][j] 
                           minutes+=1

            return minutes
Solution().orangesRotting([[0,2]])