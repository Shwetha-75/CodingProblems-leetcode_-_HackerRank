class Solution:
    def intToRoman(self, num: int) -> str:
        map={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',
             90:'XC',400:'CD',900:'CM'
             }
        pow=0
        result=[]
        num=str(num)
        index=len(num)-1
        while index>=0:
                value=int(num[index])*10**pow
                if value in map:
                   result.append(map[value])
                elif value>1 and value<5:
                     result.append(''.join(['I']*value))
                elif value>5 and value<10:
                     rem=value%5
                     result.append('V'+''.join(['I']*rem))
                elif value>10 and value<50:
                     rem=value//10
                     result.append(''.join(['X']*rem))
                elif value>50 and value<100:
                     rem=value%50
                     result.append('L'+''.join(['X']*(rem//10)))    
                elif value>100 and value<500:
                     rem=value//100
                     result.append(''.join(['C']*rem))
                elif value>500 and value<1000:
                     rem=value%500
                     result.append('D'+''.join(['C']*(rem//100)))     
                else:
                    result.append(''.join(['M']*(value//1000)))
                index-=1
                pow+=1
        return "".join(result[::-1])    
class TestApp:
      def testing_case_one(self):
          assert Solution().intToRoman(58)=="LVIII"
      def testing_case_two(self):
          assert Solution().intToRoman(1994)=="MCMXCIV"
      def testing_case_three(self):
          assert Solution().intToRoman(3749)=="MMMDCCXLIX"
