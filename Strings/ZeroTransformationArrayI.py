class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        count=0
        for i in nums:
            if i==0:
               count+=1 
        for query in queries:
            for i in range(query[0],query[1]+1):
                if nums[i]!=0:
                    if nums[i]-1==0:
                       count+=1
                    nums[i]-=1
        return count==len(nums)
# optimized Approach
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        diff=[0]*(len(nums)+1) 
        for query in queries:
            diff[query[0]]+=1 
            diff[query[1]+1]-=1 
        for i in range(len(diff)-1):
            diff[i]+=diff[i-1] if i>0 else 0 
            if diff[i]<nums[i]:
                return False
        return True   
class TestApp:
      def testing_case_one(self):
          assert Solution().isZeroArray([1,0,1],[[0,2]])==True 
      def testing_case_two(self):
          assert Solution().isZeroArray([4,3,2,1],[[1,3],[0,2]])==False 
        
                        
                        