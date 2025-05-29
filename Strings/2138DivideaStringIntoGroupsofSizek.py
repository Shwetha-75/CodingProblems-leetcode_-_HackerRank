class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result=[]
        for i in range(0,len(s),k):
            temp=s[i:i+k:]
            if len(temp)==k:
                result.append(temp)
            elif len(temp)<k:
                 while len(temp)<k:
                       temp+=fill
                 result.append(temp)
        return result 

class TestApp:
      def testing_case_one(self):
          assert Solution().divideString("abcdefghi",3,"x")==["abc","def","ghi"] 
      def testing_case_two(self):
          assert Solution().divideString("abcdefghij",3,"x")==["abc","def","ghi","jxx"] 
