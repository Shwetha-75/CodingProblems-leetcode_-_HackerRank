class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        length=len(s)
        if t==0: return length 
        hash_map={}
        for char in s:
            if char in hash_map:
               hash_map[char]+=1 
            else:
                hash_map[char]=1 
                
        while t:
            temp={}
            for char in hash_map.keys():
                count_number=nums[ord(char)-ord('a')]
                initial_value= chr(ord(char)+1) if char!='z' else 'a'
                
                while count_number:
                      if initial_value in temp:
                          temp[initial_value]+=hash_map[char]
                      else:
                          temp[initial_value]=hash_map[char]
                      if initial_value=='z':
                         initial_value='a'
                      else:
                          initial_value=chr(ord(initial_value)+1)
                      count_number-=1 
            
            
            length=sum(temp.values())
            hash_map=temp
            t-=1
        return length%(10**9+7)  
class TestApp:
      def testing_case_one(self):
          assert Solution().lengthAfterTransformations("abcyy",2,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])==7
      def testing_case_two(self):
          assert Solution().lengthAfterTransformations("azbk",1,[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])==8