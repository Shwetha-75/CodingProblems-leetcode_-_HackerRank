class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        large=len(s)
        small=0 
        result=[]
        for char in s:
            if char=='D':
               result.append(large)
               large-=1 
            else:
                result.append(small)
                small+=1
        result.append(small if s[-1]=='I' else large)
        return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().diStringMatch("IDID")==[0,4,1,3,2]
      def testing_case_two(self):
          assert Solution().diStringMatch("III")==[0,1,2,3]