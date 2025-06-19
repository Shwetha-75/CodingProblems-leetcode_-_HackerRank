from collections import defaultdict
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        moves=0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            moves+=abs(seats[i]-students[i])
            
        return moves 
class TestApp:
      def testing_case_one(self):
          assert Solution().minMovesToSeat([3,1,5],[2,7,4])==4 
      def testing_case_two(self):
          assert Solution().minMovesToSeat([4,1,5,9],[1,3,2,6])==7 
      def testing_case_three(self):
          assert Solution().minMovesToSeat([2,2,6,6],[1,3,2,6])==4