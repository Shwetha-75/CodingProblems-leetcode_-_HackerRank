class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        count=0 
        for i in nums:
            if i==0:
               count+=1 
        temp=0
        for query in queries:
            for i in range(query[0],query[1]+1):
                if nums[i]!=0:
                    if nums[i]-query[2]==0:
                        count+=1 
                        nums[i]=0
                    elif nums[i]-query[2]>0:
                        nums[i]-=query[2]
            temp+=1
            if count==len(nums):
                return temp
        return temp if count==len(nums) else -1 
class TestApp:
      def testing_case_one(self):
          assert Solution().minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]])==2
      def testing_case_two(self):
          assert Solution().minZeroArray([4,3,2,1],[[1,3,2],[0,2,1]])==-1 
      def testing_case_three(self):
          assert Solution().minZeroArray([1,2,3,2,1],[[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]])==4
      def testing_case_four(self):
          assert Solution().minZeroArray([2],[[0,0,6],[0,0,2],[0,0,9],[0,0,5],[0,0,10]])==2    
        