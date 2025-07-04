# using stack
class Solution:
       def saveIronMan(self,string:str)->str:
           string=string.lower()
           stack=[]
           
           for char in string:
               temp=ord(char)
               if temp>=97 and temp<=122 or temp>=48 and temp<=57:
                   stack.append(char)
           
           return  stack==stack[::-1] 
class TestApp:
      def testing_case_one(self):
          assert Solution().saveIronMan("I am :IronnorI Ma, i")==True 
      def testing_case_two(self):
          assert Solution().saveIronMan("Ab?/Ba")==True