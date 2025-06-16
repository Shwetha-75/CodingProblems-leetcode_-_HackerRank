'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
 

Constraints:

rec1.length == 4
rec2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1 and rec2 represent a valid rectangle with a non-zero area.


'''
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
          if rec1[0]>=rec2[2] or rec2[0]>=rec1[2]: return False 
          if rec1[1]>=rec2[3] or rec2[1]>=rec1[3]: return False 
          return True 
class TestApp:
      def testing_case_one(self):
          assert Solution().isRectangleOverlap([0,0,2,2],[1,1,3,3])==True 
      def testing_case_two(self):
          assert Solution().isRectangleOverlap([0,0,1,1],[1,0,2,1])==False 
      def testing_case_three(self):
          assert Solution().isRectangleOverlap([0,0,1,1],[2,2,3,3])==False 
      def testing_case_four(self):
          assert Solution().isRectangleOverlap([1,1,7,5],[3,3,5,7])==True          
            