class Solution:
      def checkPermutationPalindrome(self,string:str)->bool:
            result=[]
            def helper(string:list[str],index:int,result:list[list[str]]):
                if index==len(string):
                   result.append(string[:])
                   return 
                for i in range(index,len(string)):
                    string[index],string[i]=string[i],string[index]
                    helper(string,index+1,result)
                    string[index],string[i]=string[i],string[index]
            string=list(string.replace(" ","").lower())
            helper(string,0,result)
            for res in result:
                  if res==res[::-1]: return True 
            return False 

# palindrome 

class Solution:
      def checkPermutationPalindrome(Self,string:str)->bool:
            string=string.lower()
            freq=[0]*26 
            for char in string:
                if ord('a')<= ord(char) and ord(char)>=ord('z'):
                   freq[ord(char)-97]+=1 
            # check if there exist any such char which as its odd frequency count more than once 
            oddFreq=False 
            for count in freq:
                  if count%2==1:
                     if oddFreq: return False 
                     oddFreq=True 
            return True 
 
 
 



class TestApp:
      def testing_case_one(self):
            assert Solution().checkPermutationPalindrome("Tact Coa")==True 
