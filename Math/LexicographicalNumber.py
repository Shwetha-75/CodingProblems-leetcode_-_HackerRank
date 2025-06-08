class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        array=[str(i) for i in range(1,n+1)]
        array.sort()
        
        return [int(i) for i in array] 
class TestApp:
      def testing_case_one(self):
          assert Solution().lexicalOrder(13)==[1,10,11,12,13,2,3,4,5,6,7,8,9]
      def testing_case_two(self):
          assert Solution().lexicalOrder(2)==[1,2]
      def testing_case_three(self):
          assert Solution().lexicalOrder(24)==[1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,3,4,5,6,7,8,9]
        