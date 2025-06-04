class Solution:
      def removeKdigits(self, num: str, k: int) -> str:
          stack=[num[0]]
          for i in range(1,len(num)):
              while stack and stack[-1]>num[i] and k:
                    stack.pop()
                    k-=1
              stack.append(num[i])
          while k:
               stack.pop()
               k-=1
          return str(int("0"+"".join(stack))) 
class TestApp:
      def testing_case_one(self):
          assert Solution().removeKdigits("1432219",3)=="1219"
      def testing_case_two(self):
          assert Solution().removeKdigits("10200",1)=="200"
      def testing_case_three(self):
          assert Solution().removeKdigits("10",2)=="0"