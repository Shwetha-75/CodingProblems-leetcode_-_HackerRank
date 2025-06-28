class Solution:
      def reverseString(self,s:str):
          s=s.split(" ")
          n=len(s)
          for i in range(n):
              s[i]=s[i][::-1]
          return " ".join(s)
class TestApp:
    def testing_case_one(self):
        assert Solution().reverseString("Let's take LeetCode contest")=="s'teL ekat edoCteeL tsetnoc"
    