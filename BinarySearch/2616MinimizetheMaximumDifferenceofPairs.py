import sys
import heapq
class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        result=sys.maxsize
        print(nums)
        for i in range(len(nums)-1):
            array=[-1*abs(nums[i]-nums[i+1])]
            temp=p-len(array)
            index=i+2
            # print(i)
            if len(nums[index::])//2==temp:
                for j in range(index,len(nums)-1,2):
                    heapq.heappush(array,-1*abs(nums[j]-nums[j+1]))
                    # print(array,temp,len(nums[index::]),index,i)
            elif len(nums[index::])>temp:
                while temp!=0:
                      min_value=sys.maxsize
                      
                      for k in range(index,len(nums)-1):
                          diff=abs(nums[k]-nums[k+1])
                          if diff<min_value:
                             min_value=diff
                             index=j+1
                          print(diff,nums[k],nums[k+1])
                      temp-=1
                      index+=1
                      heapq.heappush(array,-1*min_value)
            print("When i:",i,"array: ",array)    
            if len(array)==p:
               result=min(result,-1*heapq.heappop(array))
        return result   
Solution().minimizeMax([3,0,5,0,0,1,6],3)
class TestApp:
      def testing_case_one(self):
          assert Solution().minimizeMax([10,1,2,7,1,3],2)==1
      def testing_case_two(self):
          assert Solution().minimizeMax([4,2,1,2],1)==0
      def testing_case_three(self):
          assert Solution().minimizeMax([3,4,2,3,2,1,2],3)==1
      def testing_case_four(self):
          assert Solution().minimizeMax([3,3,5,1,0,5,6,6],4)==1
      def testing_case_five(self):
          assert Solution().minimizeMax([1,1,0,3],2)==2
      def testing_case_six(self):
          assert Solution().minimizeMax([3,11,4,3,5,7,4,4,5,5],3)==0
      def testing_case_seven(self):
          assert Solution().minimizeMax([6,7,0,5,3,6],3)==3