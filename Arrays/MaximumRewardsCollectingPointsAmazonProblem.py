'''
Problem Statement (Amazon Shopping Reward Points) SDE II Intern 

You are given n items, each with a reward point value in pointValues[i]. You can purchase each item at most once.

When you purchase the i-th item, you earn pointValues[i] points.

After purchasing any item, the reward points of all remaining unpurchased items are reduced by 1 point each (but not below zero).

Goal:

Purchase the items in an optimal order so that the total sum of collected points is maximized.

Note:

Once an item is purchased, its value becomes 0.

The value reduction happens immediately after each purchase, to all remaining unpurchased items.

Example from the image:

Input: n = 5, pointValues = [5, 2, 2, 3, 1]
OutPut: 7
 
You must choose an order of purchases to maximize your total points

-solution by Shwetha K 

'''

class Solution:
      def collectMaximumPoints(self,array:list[int],n:int):
          total,n=0,len(array)
          array.sort(reverse=True)
          for i in range(n):
              total+=array[i]
              for j in range(n):
                  if not array[j]:
                      continue 
                  array[j]-=1
          return total 
      
import heapq
# Optimized Approach 
class Solution:
      def collectMaximumPoints(self,array:list[int],n:int):
          array.sort(reverse=True)
          array=[-1*value for value in array]
          total,one_decrement_operations=0,0
          while True:
                sum_value=-1*heapq.heappop(array)-one_decrement_operations 
                if sum_value<=0:
                    return total 
                total+=sum_value 
                one_decrement_operations+=1
                heapq.heappush(array,0)
            
class TestApp:
      def testing_case_one(self):
          assert Solution().collectMaximumPoints([1,3,5,1,2],5)==7 
      def testing_case_two(self):
          assert Solution().collectMaximumPoints([5,3,2,2,1],5)==7 
      def testing_case_three(self):
          assert Solution().collectMaximumPoints([5,5,5],3)==12
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          