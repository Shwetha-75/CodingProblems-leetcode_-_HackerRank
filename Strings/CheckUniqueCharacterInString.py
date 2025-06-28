

# Brute Force Approach Time Complexity O(N) and Space Complexity : O(26) ~ O(1)
class Solution:
      def checkUnique(self,word:str)->bool:
        if len(word)==1: return True
        #   using Hash map 
        hash_map={}
        for letter in word:
            if letter in hash_map: return False 
            hash_map[letter]=1 
        return True 
# without using additional data structure 
class Solution:
      def checkUnique(self,word:str)->bool:
          if len(word)==1: return True 
          word=sorted(word.lower()) # sorting takes O(NlogN)==> Merge Sort Sort and Insertion Sort => Trim Sort 
          left=0
        #   O(N)
          while left<len(word)-1:
               if word[left]==word[left+1]: return False 
               left+=1 
               
          return True # Total Time Complexity : O(NlogN) space :O(N)
# using array data structure with Time Complexity : O(N) and space O(26) ~ O(1) 
class Solution:
      def checkUnique(self,word:str):
          arr=[False]*26 
          for letter in word:
              if arr[ord(letter)-97]: 
                 
                  return False 
              arr[ord(letter)-97]=True 
          
          return True 
# Using bit manipulation Time Complexity O(N) and space complexity : O(1)
class Solution:
      def checkUnique(self,word:str)->bool: 
          checker=0 
          for letter in word:
              val= 1 << ord(letter)-97 
              if checker & val >0: return False 
              checker|=val 
          return True 

class TestApp:
      def testing_case_one(self):
          assert Solution().checkUnique("abbcd")==False 
      def testing_case_two(self):
          assert Solution().checkUnique("listen")==True 
      def testing_case_three(self):
          assert Solution().checkUnique("peacock")==False 
      def testing_case_four(self):
          assert Solution().checkUnique("word")==True 
      def testing_case_five(self):
          assert Solution().checkUnique("opac")==True 
      