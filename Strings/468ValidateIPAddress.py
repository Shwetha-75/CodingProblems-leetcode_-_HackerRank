class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            #   IPV4 
            if queryIP.count(".")!=3:
                return "Neither"
            array=queryIP.split(".")
            for arr in array:
                if (arr[0]==0 and len(arr)>1) or not arr.isdigit() or (not (int(arr)>=0 and int(arr)<=255)):
                   return "Neither"
            return "IPv4"
        else:
            # IPV6 
            if queryIP.count(":")!=7:
                return "Neither"
            array=queryIP.split(":")
            for arr in array:
                if not (len(arr)>=1 and len(arr)<=4) or not self.checkCharacters(arr):
                   return "Neither"
                
            return "IPv6"
    def checkCharacters(self,node:str):
            if node.isdigit():
               return True 
            lowerCase_lower_limit=ord("a")
            lowerCase_upper_limit=ord("f")
            upperCase_lower_limit=ord("A")
            upperCase_upper_limit=ord("F")
            for character in node:
                if character.isdigit(): continue 
                if not character.isupper() and not (ord(character)>=lowerCase_lower_limit and ord(character)<=lowerCase_upper_limit):
                    return False 
                elif character.isupper() and not (ord(character)>=upperCase_lower_limit and ord(character)<=upperCase_upper_limit):
                    return False 
            return True 
                     
class TestApp:
      def testing_case_one(self):
          assert Solution().validIPAddress("172.16.254.1")=="IPv4"
      def testing_case_two(self):
          assert Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")=="IPv6"
      def testing_case_three(self):
          assert Solution().validIPAddress("256.256.256.256")=="Neither"
      def testing_case_four(self):
          assert Solution().validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")=="IPv6"
      def testing_case_five(self):
          assert Solution().validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334")=="IPv6"
      def testing_case_six(self):
          assert Solution().validIPAddress("2001:0db8:85a3::8A2E:037j:7334")=="Neither"
      def testing_case_seven(self):
          assert Solution().validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")=="Neither"
      def testing_case_eight(self):
          assert Solution().validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334")=="Neither"             
      def testing_case_nine(self):
          assert Solution().validIPAddress("f:f:f:f:f:f:f:f")=="IPv6"              
               
           