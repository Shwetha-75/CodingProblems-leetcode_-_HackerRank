class Solution:
      def canBeIncreasing(self, nums: list[int]) -> bool:  
            if self.checkSorted(nums):
                return True 
            for i in range(1,len(nums)-1):
                if nums[i-1]>=nums[i]:
                   if self.checkSorted(nums[0:i-1:]+nums[i::]):
                       return True 
                   if self.checkSorted(nums[0:i:]+nums[i+1::]):
                       return True 
                   return False 
            return True 
      def checkSorted(self,nums):
          temp=sorted(nums)
          print(temp)
          if temp!=nums:
             return False 
          for i in range(1,len(nums)):
              if nums[i-1]==nums[i]:
                  return False 
          return True 
class Solution:
        def canBeIncreasing(self, nums: list[int]) -> bool: 
            for i in range(len(nums)):
                if self.checkSorted(nums[:i:]+nums[i+1::]):
                   return True 
            return False     
        def checkSorted(self,nums:list[int]):
            for i in range(1,len(nums)):
                if nums[i-1]>=nums[i]:
                   return False 
            return True     
    
          
class Solution:
        def canBeIncreasing(self, nums: list[int]) -> bool:
            prev=nums[0]
            delete=0
            for i in range(1,len(nums)):
                if prev<nums[i]:
                   prev=nums[i]
                else:
                    if delete>=1:
                        return False 
                    delete+=1
                    if i==1 or nums[i-2]<nums[i]:
                       prev=nums[i]
            return True   
                                  
            
class TestApp:
      def testing_case_one(self):
          assert Solution().canBeIncreasing([1,2,10,5,7])==True 
      def testing_casE_two(self):
          assert Solution().canBeIncreasing([2,3,1,2])==False 
      def testing_case_three(self):
          assert Solution().canBeIncreasing([1,1,1])==False 
      def testing_case_four(self):
          assert Solution().canBeIncreasing([105,924,32,968])==True 
      def testing_case_five(self):
          assert Solution().canBeIncreasing([1,2,3,4])==True 