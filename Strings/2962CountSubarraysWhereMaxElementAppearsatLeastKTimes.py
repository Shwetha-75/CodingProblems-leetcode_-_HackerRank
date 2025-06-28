class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        count=0 
        max_element=max(nums)
        if nums.count(max_element)<k:
            return 0 
        temp=1
        for i in range(len(nums)):
            if nums[i]==max_element:
                nums[i]=1 
                
            else:
                nums[i]=0
        for i in range(len(nums)):
            temp=0
            for j in range(i,len(nums)):
                if nums[j]==1:
                    temp+=1 
                if temp>=k:
                    count+=1
        return count 
class Solution:
      def countSubarrays(self, nums: list[int], k: int) -> int:
          start=freq=end=count=0
          max_element=max(nums)
          flag=False 
          while end<len(nums):
                if nums[end]==max_element:
                   freq+=1
                if freq>=k:
                    if nums[end]==max_element:
                        if not (start==0 and nums[start]==max_element) or flag:
                           start+=1 
                        else:
                            flag=True 
                        while nums[start]!=max_element:
                              start+=1 
                    
                    count+=start+1 
                    
                end+=1 
          return count
  
class TestApp:
      def testing_case_one(self):
          assert Solution().countSubarrays([1,3,2,3,3],2)==6 
      def testing_case_two(self):
          assert Solution().countSubarrays([1,4,2,1],3)==0
      def testing_case_three(self):
          assert Solution().countSubarrays([21,11,13,15,16,21,8,9,6,21],2)==10