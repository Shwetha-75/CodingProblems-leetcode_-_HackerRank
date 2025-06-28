class Solution:
      def maximumDifference(self, nums: list[int]) -> int:
            n=len(nums)
            max_diff=-1
            for i in range(n):
                stack=[nums[i]]
                for j in range(i+1,n):
                    if stack[-1]<nums[j]:
                       stack.append(nums[j])
                if len(stack)>1:
                   max_diff=max(max_diff,stack[-1]-stack[0])
            return max_diff 
# Optimized Approach 
class Solution:
      def maximumDifference(self, nums: list[int]) -> int:
          ans=-1 
          max_value=nums[-1]
          for i in range(len(nums)-2,-1,-1):
              if nums[i]>=max_value:
                 max_value=nums[i]
              else:
                  ans=max(ans,max_value-nums[i])
          return ans
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumDifference([7,1,5,4])==4 
      def testing_case_two(self):
          assert Solution().maximumDifference([9,4,3,2])==-1
      def testing_case_three(self):
          assert Solution().maximumDifference([1,5,2,10])==9         

                  