class Solution:
        def findDuplicateNumbers(self,array:list[int])->int:
            fast=slow=0
            while True:
                  slow=array[slow]
                  fast=array[array[fast]]
                  if slow==fast:
                     break 
            ptr=0 
            while ptr!=slow:
                  ptr=array[ptr]
                  slow=array[slow]
            return ptr
                   
class TestApp:
        def testing_case_one(self):
            assert Solution().findDuplicateNumbers([1,3,4,2,2])==2 
        def testing_case_two(self):
            assert Solution().findDuplicateNumbers([3,1,3,4,2])==3
        def testing_case_three(self):
            assert Solution().findDuplicateNumbers([3,3,3,3,3])==3 
        def testing_case_four(self):
            assert Solution().findDuplicateNumbers([2,5,9,6,9,3,8,9,7,1])==9