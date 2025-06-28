class Solution:
      def rotatingString(self,s1:str,s2:str)->bool:
            s1=list(s1)
            s2=list(s2)
            if len(s1)!=len(s2): return False 
            i=0
            while i<len(s1):
                  if s1==s2 :return True 
                  s2.append(s2.pop(0))
                  i+=1 
            return s1==s2


# class Solution:
#      def rotatingString(self,s1:str,s2:str)->bool:
#          s2+=s2 
#          return s1 in s2
     
class TestApp:
      def testing_case_one(self):
          assert Solution().rotatingString("waterbottle","erbottlewat")==True 
      def testing_case_two(self):
          assert Solution().rotatingString("shwethahasadream","dreamshwethahasa")==True
          
          
print(list("adcsj"))