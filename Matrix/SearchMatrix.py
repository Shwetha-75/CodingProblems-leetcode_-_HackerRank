'''

74. Search a 2D Matrix


You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104


'''

# Merging all the rows to singles array since array is in matrix is in sorted order 
# Time complexity O(nlogn)
# Space complexity O(n*m)
class Solution:
      def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
          result=[]
          for mat in matrix:
              result+=mat 
          left=0
          right=len(matrix)-1
          while left<=right:
                mid=(left+right)//2 
                if result[mid]==target:
                    return True 
                elif result[mid]<target:
                     left=mid+1
                else:
                    right=mid-1
          return False 
# Apply Binary Search 
class Solution:
      def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
          max_row=len(matrix)
          max_col=len(matrix[0])
          row,col=max_row-1,0 
          while row>=0 and col<max_col:
                if matrix[row][col]==target:
                   return True 
                elif matrix[row][col]>target:
                    row-=1
                else:
                    col+=1
          return False 
class TestApp:
      def testing_case_one(self):
          assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)==False 
      def testing_case_two(self):
          assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)==True 
    