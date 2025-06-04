class Solution:
      def spiralMatrixTraversal(self,matrix:list[list[int]])->list[int]:
            row=len(matrix)
            col=len(matrix[0])
            result=[]
            i=j=0
            while len(result)<row*col:
                  # first row --> row is constant and column is varied
                  for k in range(j,col-j):
                      result.append(matrix[i][k])
                  print("first row",result)
                  # last column --> column constant and row is varied 
                  for k in range(i+1,row-i):
                      result.append(matrix[k][col-j-1])
                  print("last column ",result)
                  if len(result)==row*col: break   
                  # last row --> row constant and column is varied 
                  for k in range(col-j-2,j-1,-1):
                      result.append(matrix[row-i-1][k])
                  print("last row",result)
                      
                  # first col --> column constant and row is varied 
                  for k in range(row-i-2,i,-1):
                      result.append(matrix[k][j])
                  print("first col",result)
                      
                  j+=1
                  i+=1
            return result 
Solution().spiralMatrixTraversal([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
                