class Solution:
      def binaryToInteger(self,bits):
          pow=0 
          value=0 
          for i in bits:
              value+=(2**pow)*int(i)
              pow+=1
          return value
      def reverseBits(self, n: int) -> int:
          bits=list(str(bin(n))[2::])
          diff=32-len(bits)
          bits=['0']*diff+bits
          return self.binaryToInteger(bits)
class TestApp:
      def testing_case_one(self):
          assert Solution().reverseBits(43261596)==964176192
        

          