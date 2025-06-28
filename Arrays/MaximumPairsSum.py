class Solution:
      def arrayPairSum(self, nums: list[int]) -> int:
          n=len(nums)
          arr_1=[0]*(n//2) 
          arr_2=[0]*(n//2)
          index=0
          for i in range(0,n,2):
              arr_1[index]=nums[i]
              index+=1
          index=0
          for i in range(1,n,2):
              arr_2[index]=nums[i]
              index+=1
          return min(sum(arr_1),sum(arr_2))