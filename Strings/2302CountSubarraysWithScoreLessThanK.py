class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        count=0 
        for i in range(len(nums)):
            temp=0
            length=0 
            for j in range(i,len(nums)):
                temp+=nums[j]
                length+=1 
                if temp*length<k:
                    count+=1 
                else:
                    break 
        return count 
class Solution:
      def countSubarrays(self, nums: list[int], k: int) -> int:
            count=start=window_sum=end=0
            while end<len(nums):
                window_sum+=nums[end]
                if end >0 and  nums[end]<k:
                  
                   count+=1
                if window_sum*(end-start+1)<k:
                    
                    count+=1 
                else:
                    
                    while window_sum*(end-start+1)>k:
                          window_sum-=nums[start]
                          print(window_sum)
                          start+=1 
                    if start<end and end==len(nums)-1 and window_sum*(end-start+1):
                        print("yes")
                        count+=1
                end+=1 
            print(count)
class Solution:
      def countSubarrays(self, nums: list[int], k: int) -> int:
          count=start=end=total=0
          while end<len(nums):
                total+=nums[end]
                while start<=end and total*(end-start+1)>=k:
                      total-=nums[start]
                      start+=1 
                count+=end-start+1 
                end+=1
          return count 

class TestApp:
      def testing_case_one(self):
          assert Solution().countSubarrays([2,1,4,3,5],10)==6 
      def testing_case_two(self):
          assert Solution().countSubarrays([1,1,1],5)==5
      def testing_case_three(self):
          assert Solution().countSubarrays([5,2,6,8,9,7],50)==13