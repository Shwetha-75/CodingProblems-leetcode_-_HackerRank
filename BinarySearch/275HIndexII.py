'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in non-descending order, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

You must write an algorithm that runs in logarithmic time.

 

Example 1:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,2,100]
Output: 2
 

Constraints:

n == citations.length
1 <= n <= 105
0 <= citations[i] <= 1000
citations is sorted in ascending order.
'''
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if len(citations)==1:
            return 0 if not citations[0] else 1
        left,right,n=0,len(citations)-1,len(citations)
        prev=0
        while left<=right:
              mid=(left+right)//2 
            #   count of number of publishers
              count=n-mid 
              if citations[mid]>=count:
                #   taking max h-index
                  prev=max(prev,n-mid)
                # if the number of publishers is not satisfying the number of articles at 
                # present citations we wil check in right subArray
              if count>citations[mid]:
                  left=mid+1
                # Left SubArray
              else:
                  right=mid-1        
        return prev 
Solution().hIndex([0,0])
class TestApp:
      def testing_case_one(self):
          assert Solution().hIndex([0,1,3,5,6])==3
      def testing_case_two(self):
          assert Solution().hIndex([1,2,100])==2
      def testing_case_three(self):
          assert Solution().hIndex([0,1])==1 
      def testing_case_four(self):
          assert Solution().hIndex([0,0])==0        
        