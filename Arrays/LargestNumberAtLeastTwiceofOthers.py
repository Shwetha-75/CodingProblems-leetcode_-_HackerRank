class Solution:
      def dominantIndex(self, nums: list[int]) -> int:
          max_element=max(nums)
          index=nums.index(max_element)
          for i in range(len(nums)):
              if i==index:
                  continue 
              if max_element<nums[i]*2:
                  return -1 
          return index
class TestApp:
      def testing_case_one(self):
          assert Solution().dominantIndex([3,6,1,0])==1
      def testing_case_two(self):
          assert Solution().dominantIndex([1,2,3,4])==-1
