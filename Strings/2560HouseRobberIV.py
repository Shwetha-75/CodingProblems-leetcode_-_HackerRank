import sys
class Solution:
    def __init__(self):
        self.result=[]
    def minCapability(self, nums: list[int], k: int) -> int:
        min_cost=sys.maxsize
        for i in range(len(nums)-k):
            self.helper(i,[],len(nums),k,nums)
            for arr in self.result:
                min_cost=min(min_cost,max(arr))
            self.result=[] 
        return min_cost
    def helper(self,index,subset:list[int],n,k,nums):
        if index>=n or len(subset)>=k:
           if len(subset)>=k:
                self.result.append(subset[:])
           return 
        subset.append(nums[index])
        self.helper(index+2,subset,n,k,nums)
        subset.pop(-1)
        self.helper(index+1,subset,n,k,nums)
        

Solution().minCapability([5038,3053,2825,3638,4648,3259,4948,4248,4940,2834,109,5224,5097,4708,2162,3438,4152,4134,551,3961,2294,3961,1327,2395,1002,763,4296,3147,5069,2156,572,1261,4272,4158,5186,2543,5055,4735,2325,1206,1019,1257,5048,1563,3507,4269,5328,173,5007,2392,967,2768,86,3401,3667,4406,4487,876,1530,819,1320,883,1101,5317,2305,89,788,1603,3456,5221,1910,3343,4597],28)
class TestApp:
      def testing_case_one(self):
          assert Solution().minCapability([2,3,5,9],2)==5 
      def testing_case_two(self):
          assert Solution().minCapability([2,7,9,3,1],2)==2