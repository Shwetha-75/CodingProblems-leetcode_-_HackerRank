class Solution:
      def numSubmat(self, mat: list[list[int]]) -> int:
          row=len(mat)
          col=len(mat[0])
          
          for i in range(row):
 
              for j in range(col):
                  sub_mat=mat[:i+1:][:j+1:]
                  row_sub_mat=len(sub_mat)
                  col_sub_mat=len(sub_mat[0])
                  print(row_sub_mat,col_sub_mat)
                  for m in range(row_sub_mat):
                 
                      for n in range(col_sub_mat):
                          print("",sub_mat[m][n],"",end=" ")
              
                  print()
             
Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]])                  

