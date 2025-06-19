class Solution:
      def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
          rect_a_area=(ax2-ax1)*(ay2-ay1)
          rect_b_area=(bx2-bx1)*(by2-by1)
          intersection_area=max(min(ax2,bx2)-max(ax1,bx1),0)*max(min(ay2,by2)-max(ay1,by1),0)
          return rect_a_area+rect_b_area-intersection_area
class TestApp:
      def testing_case_one(self):
          assert Solution().computeArea(-3,0,3,4,0,-1,9,2)==45 
      def testing_case_two(self):
          assert Solution().computeArea(-2,-2,2,2,-2,-2,2,2)==16