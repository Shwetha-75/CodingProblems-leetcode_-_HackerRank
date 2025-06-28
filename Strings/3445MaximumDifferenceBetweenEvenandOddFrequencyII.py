'''
You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

subs has a size of at least k.
Character a has an odd frequency in subs.
Character b has an even frequency in subs.
Return the maximum difference.

Note that subs can contain more than 2 distinct characters.

 

Example 1:

Input: s = "12233", k = 4

Output: -1

Explanation:

For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

Example 2:

Input: s = "1122211", k = 3

Output: 1

Explanation:

For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

Example 3:

Input: s = "110", k = 3

Output: -1

 

Constraints:

3 <= s.length <= 3 * 104
s consists only of digits '0' to '4'.
The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
1 <= k <= s.length

'''

import heapq
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        diff=float('-inf')
        for m in range(len(s)):
            hash_map={}
            count=0 
            for i in range(m,min(len(s),m+k)):
                
                char=s[i]
                if char not in hash_map:
                    hash_map[char]=1
                else:
                    hash_map[char]+=1
                count+=1
                if count>=k:
                    temp=list(hash_map.items())
                    odd_value=[-1*value[1] for value in temp if value[1]%2]
                    even_value=[value[1] for value in temp if not value[1]%2]
                    heapq.heapify(odd_value)
                    heapq.heapify(even_value)
                    if odd_value and even_value:
                       odd=-1*(heapq.heappop(odd_value) if odd_value else 0)
                       even=heapq.heappop(even_value) if even_value else 0
                       if odd != even:
                           diff=max(diff,odd-even)
                    for j in range(i+1,len(s)):
                        char=s[j]
                        if char not in hash_map:
                            hash_map[char]=1
                        else:
                            hash_map[char]+=1
                        temp=list(hash_map.items())
                        odd_value=[-1*value[1] for value in temp if value[1]%2]
                        even_value=[value[1] for value in temp if not value[1]%2]
                        heapq.heapify(odd_value)
                        heapq.heapify(even_value)
                        if odd_value and even_value:
                           odd=-1*(heapq.heappop(odd_value) if odd_value else 0)
                           even=heapq.heappop(even_value) if even_value else 0
                           if odd!=even:
                               diff=max(diff,odd-even)
        return diff 
class TestApp:
      def testing_case_one(self):
          assert Solution().maxDifference("12233",4)==-1
      def testing_case_two(self):
          assert Solution().maxDifference("1122211",3)==1
      def testing_case_three(self):
          assert Solution().maxDifference("110",3)==-1
      def testing_case_four(self):
          assert Solution().maxDifference("44114402",7)==1