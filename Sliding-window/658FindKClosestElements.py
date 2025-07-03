'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

'''

import heapq
class Solution:
      def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
          result,nums=[],[]
          for i in range(len(arr)):
              if k>0:
                 heapq.heappush(result,arr[i])
                 k-=1
              elif abs(result[0]-x)>arr[i]-x:
                  heapq.heappop(result)
                  heapq.heappush(result,arr[i])
          while result:
                heapq.heappush(nums,heapq.heappop(result))
          return nums
                  


class TestApp:
      def testing_case_one(self):
          assert Solution().findClosestElements([1,2,3,4,5],4,3)==[1,2,3,4]
      def testing_case_two(self):
          assert Solution().findClosestElements([1,1,2,3,4,5],4,-1)==[1,1,2,3]
      def testing_case_three(self):
          assert Solution().findClosestElements([-2,-1,1,2,3,4,5],7,3)==[-2,-1,1,2,3,4,5]