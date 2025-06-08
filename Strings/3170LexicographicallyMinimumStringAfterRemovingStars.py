#Time Limit exceeds
class Solution:
    def clearStars(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!='*':
                stack.append(char)
            else:
                self.removeCharacter(stack)
        result=[]
        for char in stack:
            if char !=-1:
                result.append(char)
        return "".join(result)
    def removeCharacter(self,stack:list[str]):
        min_character=stack[-1]
        index=len(stack)-1
        for i in range(len(stack)-2,-1,-1):
            if stack[i]<min_character:
               min_character=stack[i]
               index=i 
        stack[index]=-1
Solution().clearStars("aaba*")    
# Optimizing the code
class Solution:
      def clearStars(self, s: str) -> str:
          count=0
          index=len(s)-1
          if s[-1]=='*':
            for i in range(len(s)-1,-1,-1):
                if s[i]=='*':
                   count+=1
                   index=i 
            s:list[str]=list(s[:index])
          
          while count:
                print(index)
                min_value=s[-1]
                ind=-1
                for i in range(-2,-1,-1):
                    if s[i]<min_value:
                       min_value=s[i]
                       ind=i 
                
                s.pop(ind)
                
                count-=1 
          return "".join(s)
# Optimal Approach Using Heapq data structures  
import heapq
class Solution:
      def clearStars(self, s: str) -> str:
          stack=[]
          s=list(s)
          for index in range(len(s)):
              if s[index]=='*':
                 temp,ind=heapq.heappop(stack)
                 print(temp,ind)
                 s[-ind]=''
                 s[index]=''
              else:
                  heapq.heappush(stack,[s[index],-index])
          return "".join(s)

class TestApp:
      def testing_case_one(self):
          assert Solution().clearStars("aaba*")=="aab"
      def testing_case_two(self):
          assert Solution().clearStars("abc")=="abc"
    #   def testing_case_three(self):
          