class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        arr=[0]*len(nums)
        for i in range(len(nums)):
            arr[i]=nums[nums[i]]
        return arr[:]
class TestApp:
      def testing_case_one(self):
          assert Solution().buildArray([0,2,1,5,3,4])==[0,1,2,4,5,3] 
      def testing_case_two(self):
          assert Solution().buildArray([5,0,1,2,3,4])==[4,5,0,1,2,3]
    