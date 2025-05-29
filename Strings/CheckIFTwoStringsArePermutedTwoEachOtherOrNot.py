class Solution:
      def checkPermutation(self,s1:str,s2:str)->bool:
            result=[]
            s1=list(s1)
            def helper(index:int,s1,result:list[str]):
                if index==len(s1):
                    result.append(''.join(s1[:]))
                    return 
                for i in range(index,len(s1)):
                    s1[index],s1[i]=s1[i],s1[index]
                    helper(index+1,s1,result)
                    s1[index],s1[i]=s1[i],s1[index]
            helper(0,s1,result)
            return s2 in result 
        
class Solution:
      def checkPermutation(self,s1:str,s2:str)->bool:
          if len(s1)!=len(s2): return False 
          freq_1=[0]*26 
          freq_2=[0]*26
          for i,j in zip(s1,s2):
              
              freq_1[ord(i)-97]+=1 
              freq_2[ord(j)-97]+=1 
      
          for i in s1:
              if freq_1[ord(i)-97]!=freq_2[ord(i)-97]: return False 
          return True 


class Solution:
      def checkPermutation(self,s1:str,s2:str)->bool:
          s1=sorted(s1)
          s2=sorted(s2)
#           return s1==s2 

class TestApp:
      def testing_case_one(self):
          assert Solution().checkPermutation("abc","bca")==True 
      def testing_case_two(self):
          assert Solution().checkPermutation("abcd","abdc")==True 
      def testing_case_three(self):
          assert Solution().checkPermutation("abc","dcb")==False    