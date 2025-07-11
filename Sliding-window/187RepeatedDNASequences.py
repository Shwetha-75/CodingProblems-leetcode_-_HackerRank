'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        hash_map={}
        n=len(s)
        for i in range(n):
            temp=s[i:i+10:]
            if temp in hash_map:
                hash_map[temp]+=1
            else:
                hash_map[temp]=1
        result=[]
        for key,value in hash_map.items():
            if value>1:
                result.append(key)
        return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")==["AAAAACCCCC","CCCCCAAAAA"]
      def testing_case_two(self):
          assert Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")==["AAAAAAAAAA"]     
        