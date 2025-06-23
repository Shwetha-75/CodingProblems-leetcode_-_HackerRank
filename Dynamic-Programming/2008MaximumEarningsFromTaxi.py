class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        stack=[rides[0]]
        for i in range(1,len(rides)):
            prev=stack[-1]
            current=rides[i]
            if prev[1]>current[0]:
                amt_p=prev[1]-prev[0]+prev[2]
                amt_c=current[1]-current[0]+current[2]
                if amt_c>amt_p:
                   stack.pop()
                   stack.append(current)
            else:
                stack.append(current)
        max_value=0 
        for element in stack:
            max_value+=element[1]-element[0]+element[2]
        return max_value
class TestApp:
      def testing_case_one(self):
          assert Solution().maxTaxiEarnings(5,[[2,5,4],[1,5,1]])==7 
      def testing_case_two(self):
          assert Solution().maxTaxiEarnings(20,[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]])==20