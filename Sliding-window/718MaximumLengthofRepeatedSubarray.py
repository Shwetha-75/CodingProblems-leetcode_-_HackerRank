'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

'''
# Brute Force Approach
class Solution:
      def findLength(self, nums1: list[int], nums2: list[int]=[]) -> int:
          result,n={},len(nums1)
          for i in range(n):
              for j in range(i,n):
                  temp=str(nums1[i:j+1])
                  if temp in result:
                      result[temp]+=1
                  else:
                      result[temp]=1
          max_len=0 
          for i in range(len(nums2)):
              for j in range(i,len(nums2)):
                  temp=str(nums2[i:j+1])
                  if temp in result:
                      if len(nums2[i:j+1])>max_len:
                          max_len=len(nums2[i:j+1])            
          return max_len 
# Dynamic Programming
class Solution:
      def findLength(self, nums1: list[int], nums2: list[int]=[]) -> int:
          max_len=0
          m,n=len(nums1),len(nums2)
          dp=[[0]*(m+1) for _ in range(n+1)]
          for i in range(1,n+1):
              for j in range(1,m+1):
                  if nums1[i-1]==nums2[j-1]:
                      dp[i][j]=dp[i-1][j-1]+1
                  max_len=max(max_len,dp[i][j])
          return max_len
# Solution().findLength([70,39,25,40,7],[52,20,67,5,31])     
class TestApp:
      def testing_case_one(self):
          assert Solution().findLength([1,2,3,2,1],[3,2,1,4,7])==3 
      def testing_case_two(self):
          assert Solution().findLength([0,0,0,0,0],[0,0,0,0,0])==5 
      def testing_case_three(self):
          assert Solution().findLength([70,39,25,40,7],[52,20,67,5,31])==0      
    