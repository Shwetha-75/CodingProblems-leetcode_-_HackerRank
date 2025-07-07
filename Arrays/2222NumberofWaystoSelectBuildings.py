'''
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.

'''

# Brute Force 
class Solution:
      def numberOfWays(self, s: str) -> int:
          count,n=0,len(s)
          for i in range(n-2):
              for j in range(i+1,n-1):
                  for k in range(j+1,n):
                      if s[i]!=s[j] and s[j]!=s[k] and s[i]==s[k]:
                          count+=1
          return count 
# Optimized Approach 
class Solution:
      def numberOfWays(self, s: str) -> int:
          dp={'0':0,'1':0,'01':0,'10':0,'010':0,'101':0}
          for char in s:
              if char=='0':
                  dp['0']+=1
                  dp['10']+=dp['1']
                  dp['010']+=dp['01']
              else:
                  dp['1']+=1
                  dp['01']+=dp['0']
                  dp['101']+=dp['10']
          return dp['101']+dp['010']        
      
# with constant space and linear time complexity
class Solution:
      def numberOfWays(self, s: str) -> int:
          count0=count1=count10=count01=result=0 
          for char in s:
              if char=='0':
                  count0+=1
                  result+=count10 
                  count01+=count1
              else:
                  count1+=1
                  result+=count01
                  count10+=count0  
          return result
class TestApp:
      def testing_case_one(self):
          assert Solution().numberOfWays("001101")==6 
      def testing_case_two(self):
          assert Solution().numberOfWays("11100")==0
          