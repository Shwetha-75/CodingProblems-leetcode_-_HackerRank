class Solution:
        def repeatedSubstringPattern(self, s: str) -> bool:
            for i in range(len(s)):
                for j in range(i,len(s)-1):
                    temp=''
                    while len(temp)<len(s):
                          temp+=s[i:j+1:]
                    if temp==s:
                        return True 
            return False 
class Solution:
        def repeatedSubstringPattern(self, s: str) -> bool:
            for i in range(len(s)):
                for j in range(i,len(s)-1):
                    subString=s[i:j+1:]
                  
                    length=len(subString)
                    hash_map={}
                   
                    for k in range(0,len(s),length):
                        if subString==s[k:k+length]:
                            if s[k:k+length] in hash_map:
                               hash_map[s[k:k+length]]+=1 
                            else:
                               hash_map[s[k:k+length]]=1 
                    
                    if hash_map[subString]*length==len(s):
                        return True 
            return False 
                    
                        
Solution().repeatedSubstringPattern("aba")
class TestApp:
      def testing_case_one(self):
          assert Solution().repeatedSubstringPattern("abab")==True 
      def testing_case_two(self):
          assert Solution().repeatedSubstringPattern("aba")==False 
      def testing_case_three(self):
          assert Solution().repeatedSubstringPattern("abcabcabcabc")==True 
                  
          