'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''

class Solution:
      def findAnagrams(self, s: str, p: str) -> list[int]:
          p=list(p)
          s=list(s)
          p.sort()
          result=[]
          for i in range(len(s)-len(p)+1):
              temp=s[i:i+len(p)]
              temp.sort()
              if temp==p:
                  result.append(i)
          return result 

class TestApp:
      def testing_case_one(self):
          assert Solution().findAnagrams("cbaebabacd","abc")==[0,6]
      def testing_case_two(self):
          assert Solution().findAnagrams("abab","ab")==[0,1,2]          