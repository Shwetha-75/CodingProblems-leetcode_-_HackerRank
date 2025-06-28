class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        result=set()
        for i in range(len(digits)):
            if digits[i]==0:continue
            for j in range(len(digits)):
                if i!=j:
                   for k in range(len(digits)):
                       if i!=k and j!=k and not digits[k]%2:
                           result.add(digits[i]*100+digits[j]*10+digits[k])
        result=list(result)
        result.sort()
        return result
class TestApp:
      def testing_case_one(self):
          assert Solution().findEvenNumbers([2,1,3,0])==[102,120,130,132,210,230,302,310,312,320] 
      def testing_case_two(self):
          assert Solution().findEvenNumbers([2,2,8,8,2])==[222,228,282,288,822,828,882] 
      def testing_case_three(self):
          assert Solution().findEvenNumbers([3,7,5])==[]    
    
    