# Wrong Approach 
class Solution:
        def lengthAfterTransformations(self, s: str, t: int) -> int:
            hash_map={}
            if t==0:
                return len(s)
            for char in s:
                if char=='z':
                   if 'a' in hash_map:
                       hash_map['a']+=1 
                   else:
                       hash_map['a']=1 
                   if 'b' in hash_map:
                       hash_map['b']+=1 
                   else:
                       hash_map['b']=1 
                else:
                    temp=chr(ord(char)+1)
                    if temp in hash_map:
                        hash_map[temp]+=1 
                    else:
                        hash_map[temp]=1 
            t-=1 
            length=sum(hash_map.values())
            while t:
                    temp={}
                    for char in hash_map.keys():
                        if char=='z':
                            if 'a' in temp:
                                temp['a']+=1 
                            else:
                                temp['a']=1*hash_map[char]
                            if 'b' in temp:
                                temp['b']+=1 
                            else:
                                temp['b']=1*hash_map[char]
                        else:
                            ch=chr(ord(char)+1)
                            if ch in temp:
                                temp[ch]+=1 
                            else:
                                temp[ch]=1
                    t-=1
                    hash_map=temp
                    length=sum(temp.values())
            return length 
# Exceeds TIME LIMIT 
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:  
        temp=""
        length=len(s)
        if t==0:
           return len(s)
        while t:
              for char in s:
                  if char=='z':
                     temp+='ab'
                  else:
                      temp+=chr(ord(char)+1)
              length=len(temp)
              t-=1
              s=temp[:]
              temp=""
        return length
# Succeeded
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int: 
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
                if char =='z':
                   if 'a' in temp:
                       temp['a']+=hash_map[char]
                   else:
                       temp['a']=hash_map[char]
                   if 'b' in temp:
                       temp['b']+=hash_map[char]
                   else:
                       temp['b']=hash_map[char] 
                else:
                    ch=chr(ord(char)+1)
                    if ch in temp:
                        temp[ch]+=hash_map[char]
                    else:
                        temp[ch]=hash_map[char]
            
            length=sum(temp.values())
            hash_map=temp
            t-=1
        return length 
from collections import deque
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int: 
        queue=deque([0]*26)
        for char in s:
            queue[ord(char)-97]+=1
        for _ in range(t):
            temp=queue.pop()
            queue.appendleft(temp)
            queue[1]+=temp 
        return sum(queue)%(10**9+7)     
     
class TestApp:
      def testing_case_one(self):
          assert Solution().lengthAfterTransformations("abcyy",2)==7 
      def testing_case_two(self):
          assert Solution().lengthAfterTransformations("azbk",1)==5
      def testing_case_three(self):
          assert Solution().lengthAfterTransformations("wvrjwvde",17)==14
            