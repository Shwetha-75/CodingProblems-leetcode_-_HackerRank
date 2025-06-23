class Solution:
     def maximumSwap(self, num: int) -> int:
         if num<=9:
             return num 
         num=list(str(num))
         flag=False
         for i in range(len(num)):
             if flag:
                 break
             index=0
             element=num[i]
             for j in range(i+1,len(num)):
                 if num[i]<num[j]:
                    if element<=num[j]:
                       element=num[j]
                       index=j 
             if index: 
                num[i],num[index]=num[index],num[i]
                flag=True 
               
             
         return int("".join(num))
class TestApp:
      def testing_case_one(self):
          assert Solution().maximumSwap(2736)==7236
      def testing_case_two(self):
          assert Solution().maximumSwap(9973)==9973
      def testing_case_three(self):
          assert Solution().maximumSwap(98368)==98863
      def testing_case_four(self):
          assert Solution().maximumSwap(1993)==9913
              