class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        result=set()
        for i in range(len(digits)):
            if not digits[i]:
                continue
            for j in range(len(digits)):
                if i==j:
                    continue
                for k in range(len(digits)):
                    if k==i or j==i or j==k or digits[k]%2:
                        continue 
                    result.add(int(str(f"{digits[i]}{digits[j]}{digits[k]}")))
        result=list(result)
        result.sort()
        return result
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        count=[0]*10 
        result=[]
        for digit in digits:
            count[digit]+=1 
        for i in range(1,10):
            for j in range(10):
                for k in range(0,10,2):
                    if count[i]>0 and count[j]> (j==i) and count[k]> (k==i) +(k==j):
                        result.append(i*100+j*10+k)
        return result

class TestApp:
      def testing_case_one(self):
          assert Solution().findEvenNumbers([2,1,3,0])==[102,120,130,132,210,230,302,310,312,320]
      def testing_case_two(self):
          assert Solution().findEvenNumbers([2,2,8,8,2])==[222,228,282,288,822,828,882]
      def testing_case_three(self):
          assert Solution().findEvenNumbers([3,7,5])==[]           
       