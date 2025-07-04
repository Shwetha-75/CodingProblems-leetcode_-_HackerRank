# The problem statement is simple::
# Given a string s and startIndices and endIndices, find the total count of * in a container
#  ranging [startIndices[i],endIndices[i]] where | indicates open/closed container, * indicates the *
# where we can take the count of containers if and only if it is a closed container 
#   closed container : "|**|" , count=2
#
#   Example 1 :
#      s="|**|*|*" , startIndices=[1,1] , endIndices=[5,6]
#         from [1,5]  => "|**|*", the total count is 2 
#         result=[2]
#         from [1,6] => "|**|*|", the total count is 3
#         result=[2,3]
# Brute Force Approach 
class Solution:
      def countItemsInContainer(self,s:str,startIndices:list[int],endIndices:list[int]):
          result=[]
          n=len(startIndices)
          for i in range(n):
              left=startIndices[i]-1
              right=endIndices[i]-1
              while s[left]=='*':
                    left+=1
              while s[right]=='*':
                   right-=1
              result.append(len(s[left+1:right].replace("|","")))
          return result 
# Optimized Approach using prefix sum 
class Solution:
      def countItemsInContainer(self,s:str,startIndices:list[int],endIndices:list[int]):
          result=[]
          n=len(s)
          prefixSum=[0]*n 
          leftPrefix=[-1]*n 
          rightPrefix=[-1]*n 
          count,lastIndex=0,-1
          for i in range(n):
              if s[i]=='|':
                 lastIndex=i 
              leftPrefix[i]=lastIndex 
              if s[i]=='*' and lastIndex!=-1:
                  count+=1
              prefixSum[i]=count 
        #   right prefix 
          lastIndex=-1
          for i in range(n):
              if s[i]=='|':
                  lastIndex=i 
              rightPrefix[i]=lastIndex 
          n=len(startIndices)
        
          for i in range(n):
              l=leftPrefix[startIndices[i]-1]
              r=rightPrefix[endIndices[i]-1]
              if l==-1:
                 for j in  range(startIndices[i]-1,endIndices[i],1):
                     if leftPrefix[j]!=-1:
                         l=leftPrefix[j] 
                         break 
              if r==-1:
                 for j in range(endIndices[i]-1,startIndices[i],1):
                      if rightPrefix[j]!=-1:
                         r=rightPrefix[j] 
                         break 
              if l<r:
                  result.append(prefixSum[r]-prefixSum[l])
              else:
                  result.append(0)
              
          return result
          
class TestApp:
      def testing_case_one(self):
          assert Solution().countItemsInContainer("|**|*|*",[1,1],[5,6])==[2,3]
      def testing_case_two(self):
          assert Solution().countItemsInContainer("*|*|",[1],[3])==[0]
      def testing_case_three(self):
          assert Solution().countItemsInContainer("**|**|**", [1, 2, 3, 4], [8, 7, 6, 8])==[2, 2, 2, 2]
      def testing_case_four(self):
          s="*" * 10**6 + "|" + "*" * 10**6 + "|" + "*" * 10**6
          assert Solution().countItemsInContainer(s,[1, 1_000_001, 1, 1], [3_000_001, 2_000_002, 2_000_002, 1_000_000])==[1000000, 1000000, 1000000, 0] 
      def testing_case_five(self):
          assert Solution().countItemsInContainer("||||*||||***|",[1,1,4,4,1,9],[6,9,6,13,13,13])==[1,1,1,4,4,3]