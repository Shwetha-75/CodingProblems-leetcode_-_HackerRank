class Solution:
    def __init__(self):
        self.result=set()
    def countBalancedPermutations(self, num: str) -> int:
        self.helper(list(num),0)
        numbers=list(self.result)
        count=0
        for number in numbers:
            even_cnt=odd_cnt=0
            for index in range(len(number)):
                if index%2:
                   odd_cnt+=int(number[index])%((10**9)+7)
                else:
                    even_cnt+=int(number[index])%((10**9)+7)
            if even_cnt == odd_cnt:
               count+=1
        return count   
                 
    def helper(self,input:list[str],index:int=0):
        if index==len(input):
           self.result.add("".join(input))
           return 
        for i in range(len(input)):
            input[index],input[i]=input[i],input[index]
            self.helper(input,index+1)
            input[index],input[i]=input[i],input[index]
class TestApp:
      def testing_case_one(self):
          assert Solution().countBalancedPermutations("123")==2 
      def testing_case_two(self):
          assert Solution().countBalancedPermutations("112")==1
      def testing_case_three(self):
          assert Solution().countBalancedPermutations("12345")==0
        