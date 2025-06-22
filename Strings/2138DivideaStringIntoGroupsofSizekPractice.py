class Solution:
     def divideString(self, s: str, k: int, fill: str) -> list[str]:
         result=[]
         for i in range(0,len(s),k):
             result.append(s[i:i+k:])
         if len(result[-1])<k:
             result[-1]=result[-1]+"".join([fill]*(k-len(result[-1])))
         return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().divideString("abcdefghi",3,"x")==["abc","def","ghi"]
      def testing_case_two(self):
          assert Solution().divideString("abcdefghij",3,"x")==["abc","def","ghi","jxx"]