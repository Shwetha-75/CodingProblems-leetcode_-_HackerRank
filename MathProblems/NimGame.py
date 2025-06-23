class Solution:
      def canWinNim(self, n: int) -> bool:
            if n<=3:
                return True
            # me=1
            # friend=3+me
            # while me<=n and friend<=n:
            #       me=friend+1
            #       if me>=n and friend<n:
            #           return True
            #       friend=me+3 
            
            # me=2
            # friend=3+me
            # while me<=n and friend<=n:
            #       me=friend+2
            #       if me>=n and friend<n:
            #          return True 
            #       friend=me+3  
            # me=3
            # friend=me+3
            # while me<=n and friend<=n:
            #       me=friend+3
            #       if me>=n and friend<n:
            #          return True
            #       friend=me+3
             
            # return False 
            return not n%4==0 
class TestApp:
      def testing_case_one(self):
          assert Solution().canWinNim(4)==False  
      def testing_case_two(self):
          assert Solution().canWinNim(3)==True 
      def testing_case_three(self):
          assert Solution().canWinNim(2)==True 
      def testing_case_four(self):
          assert Solution().canWinNim(8)==False 
      def testing_case_five(self):
          assert Solution().canWinNim(7)==True
      def testing_case_siz(self):
          assert Solution().canWinNim(6)==True 