class Solution:
      def plusOne(self, digits: list[int]) -> list[int]:
          i=len(digits)-2
          value=digits[-1]+1
          carry=value//10 
          digits[-1]=value%10
          
          while i>=0 and carry:
                value=digits[i]+carry
                carry=value//10
                digits[i]=value%10
                i-=1 
          if carry!=0:
             digits=[carry]+digits[:]
          
          return digits 
class TestApp:
      def testing_case_one(self):
          assert Solution().plusOne([1,2,3])==[1,2,4]
      def testing_case_two(self):
          assert Solution().plusOne([4,3,2,1])==[4,3,2,2]
      def testing_case_three(self):
          assert Solution().plusOne([9])==[1,0]
      def testing_case_four(self):
          assert Solution().plusOne([9,9,9,9])==[1,0,0,0,0]