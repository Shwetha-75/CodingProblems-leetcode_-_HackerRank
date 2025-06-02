from collections import defaultdict
class Solution:
      def candy(self, ratings: list[int]) -> int:
          result=[1]*len(ratings)
          for i in range(1,len(ratings)):
              if ratings[i-1]<ratings[i]:
                 result[i]+=result[i-1]
          for i in range(len(ratings)-1,0,-1):
              if ratings[i]<ratings[i-1]:
               
                 if result[i]>=result[i-1]:
                    result[i-1]+=result[i]
  
          return sum(result)
class TestApp:
      def testing_case_one(self):
          assert Solution().candy([1,0,2])==5
      def testing_case_two(self):
          assert Solution().candy([1,2,2])==4 
      def testing_case_three(self):
          assert Solution().candy([1,3,2,2,1])==7 
      def testing_case_four(self):
          assert Solution().candy([1,2,87,87,87,2,1])==13 
        
                   
                
            