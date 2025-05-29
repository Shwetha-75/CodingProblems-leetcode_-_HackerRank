class Solution:
      def nonSpecialCount(self, l: int, r: int) -> int: 
            non_special=0 
            def helper(number:int):
                count=1 
                for i in range(2,number):
                    if not number%i:
                       count+=1 
                    if count>2:
                       return True 
                return count!=2 
            for i in range(l,r+1):
                if helper(i):
                    non_special+=1 
            return non_special 
class TestApp:
      def testing_case_one(self):
          assert Solution().nonSpecialCount(5,7)==3 
      def testing_case_two(self):
          assert Solution().nonSpecialCount(4,16)==11