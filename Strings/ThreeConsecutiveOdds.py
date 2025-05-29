class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(1,len(arr)-1):
            if arr[i-1]%2 and arr[i]%2 and arr[i+1]%2:
                return True 
        return False 
class TestApp:
      def testing_case_one(self):
          assert Solution().threeConsecutiveOdds([2,6,4,1])==False 
      def testing_case_two(self):
          assert Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])==True 
           