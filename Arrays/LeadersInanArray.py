# Brute Force Approach 
class Solution:
    def findLeadersArray(self,nums:list[int]):
        stack,n=[],len(nums)
        for i in range(n):
            temp=nums[i]
            flag=True
            for j in range(i+1,n):
                if not temp>=nums[j]:
                    flag=False
                    False
            if flag:
                stack.append(temp)
        return stack 
# Optimized Approach 
class Solution:
      def findLeadersArray(self,nums:list[int]):
          stack,n=[nums[-1]],len(nums)
          for i in range(n-2,-1,-1):
              if stack[-1]<=nums[i]:
                  stack.append(nums[i])
          return stack[::-1]     
          
class TestApp:
      def testing_case_one(self):
          assert Solution().findLeadersArray([16, 17, 4, 3, 5, 2])==[17, 5, 2]
      def testing_case_two(self):
          assert Solution().findLeadersArray([10, 4, 2, 4, 1])==[10, 4, 4, 1]
      def testing_case_three(self):
          assert Solution().findLeadersArray([5, 10, 20, 40])==[40]
      def testing_case_four(self):
          assert Solution().findLeadersArray([30, 10, 10, 5])==[30, 10, 10, 5]
        