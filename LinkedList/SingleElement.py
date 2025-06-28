class Solution:
      def findSingleElement(self,array:list[int])->int:
            hash_map={}
        #     finding the array elements frequency 
            for num in array:
                  if num in hash_map:
                    hash_map[num]+=1
                  else: 
                      hash_map[num]=1 
            for num in array:
                if hash_map[num]==1:
                   return num 
class Solution:
      def findSingleElement(self,array:list[int])->int:
          ans=array[0]
          for i in range(1,len(array)):
              ans^=array[i]
          return ans 
          
class TestApp:
      def testing_case_one(self):
          assert Solution().findSingleElement([2,2,1])==1 
      def testing_case_two(self):
          assert Solution().findSingleElement([4,1,2,1,2])==4 
      def testing_case_three(self):
          assert Solution().findSingleElement([1])==1     
     