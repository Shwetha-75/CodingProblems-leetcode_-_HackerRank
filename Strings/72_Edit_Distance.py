
# Wrong Approach 

class Solution:
      def minDistance(self, word1: str, word2: str) -> int:
            editCount=0 
            index_1,index_2=len(word1)-1,len(word2)-1 
            while index_1>=0 and index_2>=0:
                  if word1[index_1]==word2[index_2]:
                     editCount+=1
                     index_2-=1 
                  index_1-=1 
            return len(word1)-editCount 


class TestApp:
      def testing_case_one(self):
          assert Solution().minDistance("horse","ros")==3 
      def testing_case_two(self):
          assert Solution().minDistance("intention","execution")==5 