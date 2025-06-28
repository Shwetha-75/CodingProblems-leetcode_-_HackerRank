class Solution:
    def myAtoi(self, s: str) -> int:
        stack=[]
        # checking leading white spaces 
        start=0 
        while start<len(s):
              if s[start]==' ':
                  start+=1 
              else:
                  break 
        # checking sign
        while start<len(s):
              if s[start]=='-' or s[start]=='+':
                 stack.append(s[start])
                 start+=1 
              else:
                  break

        # ignoring leading zeros 
        while start<len(s):
              if s[start]=='0':
                 start+=1
              else:
                  break 
        # checking for non digits 
        pow=0 
        value=[]
        while start<len(s):
              if ord(s[start])>=ord('0') and ord(s[start])<=ord('9'):
                 value.append(s[start])
                 start+=1
              else:
                  break 
        if stack or value:
            if stack:
                count_negative=stack.count('-')
                
                if count_negative%2:
                    sum= -int(''.join(value))
                    return -2**31 if sum<-2**31 else sum
                else:
                    sum=+int(''.join(value))
                    return +2**31 if sum>+2**31 else sum
            else:
                    sum=int("".join(value))
                    return 2**31 if sum>2**31 else  sum 
        return 0  
  
class TestApp:
      def testing_case_one(self):
          assert Solution().myAtoi("words and 987")==0
      def testing_case_two(self):
          assert Solution().myAtoi("-042")==-42
      def testing_case_three(self):
          assert Solution().myAtoi("42")==42 
      def testing_case_four(self):
          assert Solution().myAtoi("0-1")==0 
      def testing_case_five(self):
          assert Solution().myAtoi("1337c0d3")==1337 
      