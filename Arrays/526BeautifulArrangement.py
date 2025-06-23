class Solution:
      def __init__(self):
          self.array=[]
      def helper(self,index,nums):
          if index==len(nums):
             self.array.append(nums[:])
             return 
          for i in range(index,len(nums)):
              nums[index],nums[i]=nums[i],nums[index]
              self.helper(index+1,nums)
              nums[index],nums[i]=nums[i],nums[index]   
      def countArrangement(self, n: int) -> int:
            array=list(range(1,n+1))
            self.helper(0,array)
            count=1
            print(self.array)
            for i in range(1,len(self.array)):
                arr=self.array[i]
                flag=True
                print(arr)
                for j in range(0,len(arr)):
                    
                    if not(arr[j]%(j+1) or (j+1)%arr[j]):
                       flag=False 
                if flag:
                    count+=1
            return count 
Solution().countArrangement(4)
class TestApp:
      def testing_case_one(self):
          assert Solution().countArrangement(2)==2
      def testing_case_two(self):
          assert Solution().countArrangement(1)==1
          

          