class Solution:
      def isOneBitCharacter(self, bits: list[int]) -> bool:
          index=0
          while index<len(bits)-1:
                if bits[index]:
                   index+=2
                else:
                    index+=1
          return index==len(bits)-1
class TestApp:
      def testing_case_one(self):
          assert Solution().isOneBitCharacter([1,0,0])==True 
      def testing_case_two(self):
          assert Solution().isOneBitCharacter([1,1,1,0])==False 
      def testing_case_three(self):
          assert Solution().isOneBitCharacter([1,0,0,0])==True 
      def testing_case_four(self):
          assert Solution().isOneBitCharacter([1,0,0,1,0])==False