class Solution:
      def sortEvenOdd(self, nums: list[int]) -> list[int]:
        #   odd indices traversing in non-increasing order 
        odd_array=[]
        even_array=[]
        for i in range(len(nums)):
            if i%2:
               even_array.append(nums[i])
            else:
                odd_array.append(nums[i])
        odd_array.sort()
        even_array.sort(reverse=True)
        result=[0]*len(nums)
        index_1=index_2=0 
        for i in range(len(nums)):
            if i%2:
               result[i]=even_array[index_1]
               index_1+=1
            else:
                result[i]=odd_array[index_2]
                index_2+=1
        return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().sortEvenOdd([4,1,2,3])==[2,3,4,1] 
      def testing_case_two(self):
          assert Solution().sortEvenOdd([2,1])==[2,1] 