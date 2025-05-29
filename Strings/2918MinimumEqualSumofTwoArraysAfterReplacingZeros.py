class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        count_1=nums1.count(0)
        count_2=nums2.count(0)
        for i in range(len(nums1)):
            if nums1[i]==0:
               nums1[i]=1 
        for i in range(len(nums2)):
            if nums2[i]==0:
               nums2[i]=1 
        sum_1=sum(nums1)
        sum_2=sum(nums2)
        if count_1==0:
            if sum_2>sum_1:
              return -1
            elif sum_2==sum_1:
                 return sum_2 
        if count_2==0:
            if sum_1>sum_2:
               return -1 
            elif sum_2==sum_1:
                return sum_1 
        return max(sum_1,sum_2)       
class TestApp:
      def testing_case_one(self):
          assert Solution().minSum([3,2,0,1,0],[6,5,0])==12
      def testing_case_two(self):
          assert Solution().minSum([2,0,2,0],[1,4])==-1 
      def testing_case_three(self):
          assert Solution().minSum([8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0],[29,1,6,0,10,24,27,17,14,13,2,19,2,11])==179         
 
               