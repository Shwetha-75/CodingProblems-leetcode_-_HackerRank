class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        result=[]
        row_len=len(mat)
        col_len=len(mat[0])
        for diagonal in range(row_len+col_len-1):
            current_array=[]
            for row in range(row_len):
                for col in range(col_len):
                    if row+col==diagonal:
                       current_array.append(mat[row][col])
            if diagonal%2:
               result+=current_array
            else:
                result+=current_array[::-1]
        return result
class TestApp:
      def testing_case_one(self):
          assert Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])==[1,2,4,7,5,3,6,8,9]
      def testing_case_two(self):
          assert Solution().findDiagonalOrder([[1,2],[3,4]])==[1,2,3,4] 
    
 