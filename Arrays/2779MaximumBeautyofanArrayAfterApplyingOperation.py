class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        count=1
        nums.sort(reverse=True)
        stack=[nums[0]]
        for i in range(1,len(nums)):
            if stack[0]-nums[i]<=2*k:
                stack.append(nums[i])
            else:
                count=max(count,len(stack))
                temp=[]
                for num in stack:
                    if num-nums[i]<=2*k:
                        temp.append(num)
                temp.append(nums[i])
                stack=temp 
       
        return max(count,len(stack)) 
from collections import defaultdict,Counter
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        result={}
        # nums.sort()
        for num in nums:
            left=num-k 
            right=num+k 
            if left<0:
                result+=list(range(0,right+1,1))
            else:
                result+=list(range(left,right+1,1))
        hash_map=defaultdict(int)
        for element in result:
            hash_map[element]+=1
        # print(hash_map)
        result=list(hash_map.items())
        # print(result)
        result.sort(reverse=True,key=lambda x:x[1])
        return result[0][1]     
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        count=0 
        hash_map=defaultdict(int)
        for i in range(len(nums)):
            left=nums[i]-k
            right=nums[i]-k 
            if left>=0:
               if right-left<=2*k:
                   count+=1
            else:
                hash_map[nums[i]]+=1
        hash_map=list(hash_map.items())
        hash_map.sort(reverse=True,key= lambda x:x[1])
        return max(count,hash_map[0][1])       
        
Solution().maximumBeauty([43,86,33,18],23)
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumBeauty([4,6,1,2],2)==3
      def testing_case_two(self):
          assert Solution().maximumBeauty([1,1,1,1],10)==4
      def testing_case_three(self):
          assert Solution().maximumBeauty([43,86,33,18],23)==3
