from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
            result=[]
            hash_map_arr_1=defaultdict(int)
            for i in arr1:
                hash_map_arr_1[i]+=1 
            for i in arr2:
                if i in hash_map_arr_1:
                   while hash_map_arr_1[i]!=0:
                         result.append(i)
                         hash_map_arr_1[i]-=1 
                   del hash_map_arr_1[i]
            temp=list(hash_map_arr_1.items())
            temp.sort(key=lambda x:x[0])
            for value in temp:
                val=value[1]
                while val!=0:
                      result.append(value[0])
                      val-=1 
            return result 
class TestApp:
      def testing_case_one(self):
          assert Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])==[2,2,2,1,4,3,3,9,6,7,19]
      def testing_case_two(self):
          assert Solution().relativeSortArray([28,6,22,8,44,17],[22,28,8,6])==[22,28,8,6,17,44]
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  