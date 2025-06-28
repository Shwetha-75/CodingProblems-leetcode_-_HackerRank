class Solution:
        def __init__(self):
            self.result=[]
        def lengthOfLIS(self, nums: list[int]) -> int:
            self.findSubSequence(nums,[],0)
            print(self.result)
            return max(self.result,key=lambda x:len(x))
        
        def findSubSequence(self,nums:list[int],subset:list[int],index:int=0):
            if index==len(nums):
                self.result.append(subset[:])
                return 
            if subset:
                if subset[-1]<nums[index]:
                    subset.append(nums[index])
            else:   subset.append(nums[index])
            self.findSubSequence(nums,subset,index+1)
            if subset:
                subset.pop(-1)
            self.findSubSequence(nums,subset,index+1)
Solution().lengthOfLIS([0,1,0,3,2,3])
class TestApp:
      def testing_case_one(self):
          assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18])==4 
      def testing_case_two(self):
          assert Solution().lengthOfLIS([0,1,0,3,2,3])==4 
      def testing_case_three(self):
          assert Solution().lengthOfLIS([7,7,7,7,7,7,7])==1