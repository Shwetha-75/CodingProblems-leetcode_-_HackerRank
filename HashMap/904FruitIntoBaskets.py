class Solution:
      def totalFruit(self, fruits: list[int]) -> int:
        prev_index=0
        hash_map={fruits[0]:1}
        max_count=0 
        for i in range(1,len(fruits)):
          if fruits[i] in hash_map:
             hash_map[fruits[i]]+=1
             if fruits[prev_index]!=fruits[i]:
                prev_index=i 
          elif len(hash_map.keys())==2:
               max_count=max(max_count,sum(list(hash_map.values())))
               hash_map={fruits[prev_index]:i-prev_index,fruits[i]:1}
               prev_index=i 
          else:
              hash_map[fruits[i]]=1
              prev_index=i
        max_count=max(max_count,sum(list(hash_map.values())))
        return max_count
class TestApp:
    def testing_case_one(self):
        assert Solution().totalFruit([1,2,3,2,2])==4
    def testing_case_two(self):
        assert Solution().totalFruit([0,1,2,2])==3
    def testing_case_three(self):
        assert Solution().totalFruit([1,2,1])==3
    def testing_case_four(self):
        assert Solution().totalFruit([0,1,6,6,4,4,6])==5 
    def testing_case_five(self):
        assert Solution().totalFruit([1,0,1,4,1,4,1,2,3])==5

                      