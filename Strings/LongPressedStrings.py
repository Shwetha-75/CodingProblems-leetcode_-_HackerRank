class Solution:
      def isLongPressedName(self, name: str, typed: str) -> bool:
          ptr_1=ptr_2=0 
          prev=''
          while ptr_1<len(name) and ptr_2<len(typed):
                if name[ptr_1]==typed[ptr_2]:
                    prev=name[ptr_1]
                    ptr_1+=1 
                elif typed[ptr_2]==prev:
                     prev=typed[ptr_2]
                ptr_2+=1 
          return  ptr_1==len(name)
class TestApp:
      def testing_case_one(self):
          assert Solution().isLongPressedName("alex","aaleex")==True 
      def testing_casE_two(self):
          assert Solution().isLongPressedName("saeed","ssaaedd")==False 