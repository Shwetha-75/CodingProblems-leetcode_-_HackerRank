class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        def helper(number:int):
            result=""
            while number:
                  rem=number%2
                  number//=2 
                  result+=str(rem)
            return result[::-1]
        result=helper(n)
        ans=[0,0]
        for index in range(len(result)):
            if int(result[index]) and not index%2:
                ans[1]+=1
            elif int(result[index]):
                 ans[0]+=1 
        return ans 
                
class TestApp:
      def testing_case_one(self):
          assert Solution().evenOddBit(50)==[1,2]
      def testing_case_two(self):
          assert Solution().evenOddBit(2)==[0,1]