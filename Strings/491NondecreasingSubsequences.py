
# Wrong Solution
# class Solution:
#     def findSubsequences(self, nums: list[int]) -> list[list[int]]:
#         result=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 temp=[nums[i]]
#                 if temp[-1]<=nums[j]:
#                     temp.append(nums[j])
#                 if len(temp)>1 and temp not in result:
#                        result.append(temp[::])
#                 for k in range(j+1,len(nums)):
#                     if temp[-1]<=nums[k]:
#                         temp.append(nums[k])
#                     if len(temp)>1 and temp not in result:
#                        result.append(temp[::])
        
#         return result  

# Wrong output : [1,2,3,4,5,6,7,8,9,1,1,1,1]

class Solution:
    def __init__(self):
        self.result=[]
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.subsequence(nums,0,[])
        return self.result

    def subsequence(self,nums,index:int=0,subset:list[int]=[]):
        if index==len(nums):
            if len(subset)>=2 and subset not in self.result:
                self.result.append(subset[::])
            return 
        if subset:
            if subset[-1]<=nums[index]:
               subset.append(nums[index])
        else:
            subset.append(nums[index])
        self.subsequence(nums,index+1,subset)
        if subset:
            subset.pop()
        self.subsequence(nums,index+1,subset)

Solution().findSubsequences([1,3,5,7])
class TestApp:
      def testing_case_one(self):
          assert Solution().findSubsequences([4,6,7,7])==[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
      def testing_case_two(self):
          assert Solution().findSubsequences([4,4,3,2,1])==[[4,4]]
result=[]
