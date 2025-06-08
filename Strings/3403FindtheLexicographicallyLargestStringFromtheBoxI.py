'''
You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.

 

Example 1:

Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
Example 2:

Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".

 

Constraints:

1 <= word.length <= 5 * 103
word consists only of lowercase English letters.
1 <= numFriends <= word.length
'''

class Solution:
      def answerString(self, word: str, numFriends: int) -> str:
        # corner cases to split the string into 1 
          if numFriends==1:
              return word 
          n=len(word)
        #   since there is not fixed for substring
        #   considering the string of 1st group 
          result=word[:n-numFriends+1]
          for i in range(1,n):
            #   later group 
              temp=word[i:n-numFriends+1+i]
            #   check lexicographically
              if temp>result:
                  result=temp 
          
          return result  
class TestApp:
      def testing_case_one(self):
          assert Solution().answerString("bif",2)=="if"
      def testing_case_two(self):
          assert Solution().answerString("dbca",2)=="dbc"
      def testing_case_three(self):
          assert Solution().answerString("gggg",4)=="g"
      def testing_case_four(self):
          assert Solution().answerString("gh",1)=="gh"
