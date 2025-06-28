from collections import defaultdict
class Solution:
         def majorityElement(self, nums: list[int]) -> list[int]:
             hash_map=defaultdict(int)
             expected_count=len(nums)//3 
             for num in nums:
                 hash_map[num]+=1 
             result=[]
             for key,value in hash_map.items():
                 if value>expected_count:
                     result.append(key)
             return result   