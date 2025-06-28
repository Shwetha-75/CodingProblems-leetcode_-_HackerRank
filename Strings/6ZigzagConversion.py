class Solution:
    def convert(self, s: str, numRows: int) -> str:
        stacks=[[] for _ in range(numRows)]
        index=0 
        while index<len(s):
            for i in range(numRows):
                if index<len(s):
                    stacks[i].append(s[index])
                    index+=1
                else:
                    break 
            for i in range(numRows-2,0,-1):
                if index<len(s):
                    stacks[i].append(s[index])
                    index+=1 
  
        return ''.join([''.join(stack) for stack in stacks])
class TestApp:
      def testing_case_one(self):
          assert Solution().convert("PAYPALISHIRING",3)=="PAHNAPLSIIGYIR"
      def testing_case_two(self):
          assert Solution().convert("PAYPALISHIRING",4)=="PINALSIGYAHRPI" 
      def testing_case_three(self):
          assert Solution().convert("A",1)=='A'        
        
        