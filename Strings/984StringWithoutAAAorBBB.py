class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        stack=[]
        while a or b :
                write_a=False 
                if len(stack)>=2 and stack[-2]==stack[-1]:
                    if stack[-1]=='b':
                        write_a=True 
                else:
                    if a>=b:
                       write_a=True 
                if write_a:
                    stack.append('a')
                    a-=1 
                else:
                    stack.append('b')
                    b-=1 
        return ''.join(stack)           
              
class TestApp:
      def testing_case_one(self):
          assert Solution().strWithout3a3b(2,6) =='bbabbabb' 
      def testing_case_two(self):
          assert Solution().strWithout3a3b(4,6)=='bbaabbaabb'or 'bbabababab'
      
                      
                      
                      
                     
                      