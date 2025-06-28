'''
1239. Maximum Length of a Concatenated String with Unique Characters
Solved
Medium
Topics
Companies
Hint
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
'''

class Solution:                          
    def maximumConcatenatedString(self,array:list):
        # def helper(word:str):
        #     original=len(word)
        #     conversion=len(set(word))
        #     return original==conversion 
        # max_length=0
        # temp=[]
        # unique=[]
        # for i in range(len(array)):
        #     temp.append(''.join(unique))
        #     for j in range(i,len(array)):
        #         temp+=array[j]
        #         if helper(temp):
        #             max_length=max(max_length,len(temp))
        # return max_length
        
        # Back tracking
        self.max_length=0
        
        def helper(index,current:list):
            string=''.join(current)
            if len(string)>len(set(string)):
                return 
            self.max_length=max(self.max_length,len(string))
            
            for i in range(len(array)):
                helper(i+1,current+[array[i]])
        helper(0,[])
        return self.max_length
  
def main():
    sol=Solution()
    result=sol.maximumConcatenatedString( ["abcdefghijklmnopqrstuvwxyz"])
    print(result)
main()