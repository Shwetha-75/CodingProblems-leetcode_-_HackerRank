class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        count=1 
        stack=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]-stack[0]<=k:
               stack.append(nums[i])
            else:
                count+=1
                stack=[nums[i]]
        return count 
class TestApp:
      def testing_case_one(self):
          assert Solution().partitionArray([3,6,1,2,5],2)==2 
      def testing_case_two(self):
          assert Solution().partitionArray([1,2,3],1)==2
      def testing_case_three(self):
          assert Solution().partitionArray([2,2,4,5],0)==3
                
     