# Brute Force 
class Solution:
      def isOneAway(self,string1:str,string2:str)->bool:
          if len(string1) == len(string2):
              return self.stringsAreSame(string1,string2)
          elif len(string1)+1 == len(string2):
               return self.stringsAreNotSame(string1,string2)
          elif len(string1)-1 == len(string2):
              return self.stringsAreNotSame(string2,string1)
          return False 
      def stringsAreSame(self,word1:str,word2:str)->bool:
          index_1,index_2,flag=0,0,False
          while index_1 <  len(word1) and index_2 < len(word2):
                if word1[index_1]!=word2[index_2]:
                   if flag: return False 
                   flag=True
                index_1+=1 
                index_2+=1 
          return True 
      def stringsAreNotSame(self,word1:str,word2:str)->bool:
            index_1,index_2=0,0 
            while index_1 < len(word1) and index_2 < len(word2):
                  if word1[index_1] != word2[index_2]:
                      if index_1 != index_2:
                         return False 
                      index_2+=1 
                  else:
                      index_1+=1 
                      index_2+=1 
            return  True 

# Dynamic programming 

class Solution:
        def isOneAway(self,string1:str,string2:str)->bool:
            row,col=len(string1),len(string2)
            dp=[[0]*(col+1) for _ in range(row+1)]
            dp[0]=[i for i in range(col+1)]
            for i in range(row+1):
                dp[i][0]+=i 
           
            for i in range(1,row+1):
                for j in range(1,col+1):
                    if  string1[i-1]==string2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1 
           
            return dp[-1][-1]==1  
class Solution:
      def isOneAway(self,string1:str,string2:str)->bool:
            if abs(len(string1)-len(string2))>1: 
                return False 
            index_1,index_2=0,0 
            shortest=string1 if len(string1)<len(string2) else string2 
            longest=string2 if len(string1)<len(string2) else string1 
            flag=False
            while index_1 < len(string1) and index_2 < len(string2):
                  if shortest[index_1] != longest[index_2]:
                     if flag: return False 
                     flag=True 
                     if len(shortest)==len(longest):
                        index_1+=1 
                  else: index_1+=1 
                  index_2+=1 
                  
            return True 

class TestApp:
      def testing_case_one(self):
          assert Solution().isOneAway("pale","pie")==False 
      def testing_case_two(self):
          assert Solution().isOneAway("pales","pale")==True 
      def testing_case_three(self):
          assert Solution().isOneAway("pale","bale")==True 
          
      def testing_case_four(self):
          assert Solution().isOneAway("pale","bake")==False
      def testing_case_five(self):
          assert Solution().isOneAway("trvlxusommfhjaptnxgv","trvlxusommfhjaptnxgv")==True  
      def testing_case_six(self):
          assert Solution().isOneAway("oolxyloinzznw","oolxyloinzznw")==True 
      def testing_case_SEVEN(self):
          assert Solution().isOneAway("juysschlzldycttkmb","jysschlzldycttkmn")==False 
      def testing_case_eight(self):
          assert Solution().isOneAway("bedhhoygvmcatzgkyp","bedhhoygvmcatzgkbp")==True