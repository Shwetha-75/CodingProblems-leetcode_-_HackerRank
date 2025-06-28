import re
class Solution:
      def generateTag(self, caption: str) -> str:
          array=caption.split(" ")
          array=[arr for arr in array if arr]
          if not array:
              return "#"
          result=['#',array[0].lower()]
          
          for i in range(1,len(array)):
              word=list(array[i])
              if word: 
                 word[0]=word[0].upper()
                 word=word[0]+"".join(word[1::]).lower()
                 result.append(word)
              else:
                  result.append("".join(word))
          result="".join(result)
          result=re.sub("[^a-zA-Z#]","",result)
          return result[:100:]
class TestApp:
      def testing_case_one(self):
          assert Solution().generateTag("Leetcode daily streak achieved")=="#leetcodeDailyStreakAchieved"
      def testing_case_two(self):
          assert Solution().generateTag("can I Go There")=="#canIGoThere"
      def testing_case_three(self):
          assert Solution().generateTag("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")=="#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
      def testing_case_four(self):
          assert Solution().generateTag("   ")=="#"
      def testing_case_five(self):
          assert Solution().generateTag(" fghjklqewrtyuiopvbmmhjgyouy")=="#fghjklqewrtyuiopvbmmhjgyouy"           