# Brute Force Approach
class Solution:
     def rotateTheArray(self,array:list[int],k:int):
         while k!=0:
               array.insert(0,array.pop(-1))
               k-=1 
         return array
# Swapping 
class Solution:
    def rotateTheArray(self,array:list[int],k:int):
        def swapping(i:int,j:int):
            while i<=j:
                array[i],array[j]=array[j],array[i]
                i+=1
                j-=1 
        # swapping 
        length=len(array)
        k%=length 
        swapping(0,length-1)
        swapping(0,k-1)
        swapping(k,length-1)
        
          
class TestApp:
      def testing_case_one(self):
          array=[1,2,3,4,5,6,7]
          assert not Solution().rotateTheArray(array,3) and array==[5,6,7,1,2,3,4]
      def testing_case_two(self):
          array=[1,2,3,4,5]
          assert not Solution().rotateTheArray(array,2) and array==[4,5,1,2,3]
      def testing_case_three(self):
          array=[1,2,3,4,5]
          assert not Solution().rotateTheArray(array,5) and array==[1,2,3,4,5]