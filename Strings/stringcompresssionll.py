'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that are 10 or 
longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

'''

class Solution:
        def compress(self, chars: list[str]) -> int:
            # hash map
            hash_map={chars[0]:1}
            temp=chars[:]
            chars.clear()
            for i in range(1,len(temp)):
                if temp[i] in hash_map:
                    hash_map[temp[i]]+=1 
                else:
                    prev=temp[i-1]
                    if hash_map[prev]==1:
                        chars.append(prev)
                    else:
                        
                        chars.append(prev)
                    
                        chars+=list(str(hash_map[prev]))
                        
                    del hash_map[prev] 
                    hash_map[temp[i]]=1 
                    
            if hash_map[temp[-1]]==1:
                chars.append(temp[-1])
            else:
                chars.append(temp[-1])
                chars+=list(str(hash_map[temp[-1]]))
            return len(chars) 
     
                
class TestApp:
      def testing_case_one(self):
          chars=["a","a","b","b","c","c","c"]
          assert Solution().compress(chars)==6 and chars==["a","2","b","2","c","3"]
      def testing_case_two(self):
          chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
          assert Solution().compress(chars) == 4 and chars==["a","b","1","2"]
      def testing_Case_three(self):
          chars=["a"]
          assert Solution().compress(chars)==1 and chars == ["a"]