'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109

'''
# Binary Search 

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        max_row=len(matrix)
        max_col=len(matrix[0])
        row,col=max_row-1,0 
        while row>=0 and col<max_col-1:
              if matrix[row][col]==target:
                 return True 
              elif matrix[row][col]>target:
                   row-=1
              else:
                   col+=1
        return False 
class TestApp:
      def testing_case_one(self):
          assert Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)==True 
      def testing_case_two(self):
          assert Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20)==False    
    