'''
The manager of the Amazon warehouse has decided to make changes to the inventory by changing the prices of the products. Currently, the inventory has n products, where the price of the fh product is represented by the array element prices[i].

The manager is given two integers: k:- which is the maximum amount by which a product's price can be adjusted (increased or decreased) in a single operation, and d:- which represents the target price difference. The goal is to ensure that the difference between the highest and lowest prices in the inventory is strictly less than d.

In order to make changes to the inventory, the manager can do the following operation any number of times:

The manager selects two indices x y (1sx, y sn), and an integer p(1 spsk.

The manager increases the price of the product x by p.

The manager decreases the price of the product y by p.

Given n products, an array prices, and the two integers kand d, find the minimum number of operations that the manager has to perform such that the maximum difference between the prices of any two products from the array of products is strictly less than d.

Note: The array prices follows 1-based indexing meaning the first element is at index 1 rather than 0.
'''

import multiprocessing 
import time
class Solution:
      def findMinimumPossibleWays(self,array:list[int],k:int,d:int)->int:
            operations=0
            while True:
                  max_index=min_index=0 
                  for i in range(len(array)):
                      if array[i]<array[min_index]:
                          min_index=i 
                      if array[i]>array[max_index]:
                          max_index=i 
                  current_diff=array[max_index]-array[min_index]
                  if current_diff<d:
                      return operations 
                  p=min(k,current_diff//2)
                  array[max_index]-=p
                  array[min_index]+=p 
                  operations+=1
# Optimized Approach 
class Solution:
      def findMinimumPossibleWays(self,array:list[int],k:int,d:int)->int:
               
          pass 
class TestApp:
      def testing_case_one(self):
          assert Solution().findMinimumPossibleWays([1,5,9,11],4,2)==3
      def testing_case_two(self):
          assert Solution().findMinimumPossibleWays([3,8,10,13],3,5)==1 
      def testing_case_three(self):
          assert Solution().findMinimumPossibleWays([2,3,2,3],2,2)==0
          
      def testing_case_four(self):
          
          def helper(result_dic):
              result_dic['result4']=Solution().findMinimumPossibleWays([2, 4, 6, 10],4,6)
          manager=multiprocessing.Manager()
          result_dic=manager.dict()
          p=multiprocessing.Process(target=helper,args=(result_dic))
          p.start()
          p.join(timeout=5)
          if p.is_alive():
              p.terminate()
              p.join()
              print("Time Limit Exceeded")
          else:
              assert result_dic['result4']==1
                
                
          
    