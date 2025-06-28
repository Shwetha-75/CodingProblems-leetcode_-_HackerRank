class Solution:
        def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
            n=len(nums)
            count=0
            for i in range(n):
                flagMin=flagMax=False 
                for j in range(i,n):
                    if nums[j]==minK and not flagMin:
                        flagMin=True 
                    if nums[j]==maxK and not flagMax:
                        flagMax=True 
                    if nums[j]>maxK and nums[j]<minK: break 
                    if nums[j]<=maxK and nums[j]>=minK and flagMin and flagMax:
                       count+=1 
            return count 
class Solution:
      def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
          count,n=0,len(nums) 
          minPos=maxPos=leftBound=-1 
          for i in range(n):
              if nums[i]>maxK or nums[i]<minK:
                 leftBound=i 
              if nums[i]==minK:
                  minPos=i 
              if nums[i]==maxK:
                  maxPos=i 
              count+=max(0,min(minPos,maxPos)-leftBound)
          return count                                  
class TestApp:
      def testing_case_one(self):
          assert Solution().countSubarrays([1,3,5,2,7,5],1,5)==2 
      def testing_case_two(self):
          assert Solution().countSubarrays([1,1,1,1],1,1)==10