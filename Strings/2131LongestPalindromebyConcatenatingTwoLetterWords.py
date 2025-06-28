class Solution:
     def longestPalindrome(self, words: list[str]) -> int:
        hash_reverse={}
        hash_mirror={}
        for word in words:
            if word==word[::-1]:
               if word in hash_mirror:
                   hash_mirror[word]+=1
               else: hash_mirror[word]=1
            else:
                if word in hash_reverse:
                    hash_reverse[word][0]+=1
                elif word[::-1] in hash_reverse:
                     hash_reverse[word[::-1]][1]=word 
                     hash_reverse[word]=[1,word[::-1]]
                else:
                    hash_reverse[word]=[1,'']
        # remove the hash_mirror 
        temp=hash_reverse.copy()
        for key,value in temp.items():
            if not value[1]:
                del hash_reverse[key]
        # find the maximum among
        result=0
        if hash_mirror:
            max_key=max(hash_mirror.items(),key=lambda x:x[1]) 
            if max_key:
                result+=max_key[1]*2
                del hash_mirror[max_key[0]]
                if max_key[1]!=1:
                #    check if the max_key is even then you can take maximum odd value 
                     if not max_key[1]%2:
                            odd_key_max=max(hash_reverse.items(),key=lambda x:x[1] and x[1]%2)
                            if odd_key_max: 
                               result+=odd_key_max[1]*2 
                               del hash_mirror[odd_key_max[0]]
                            for key,value in hash_mirror.items():
                                 if value%2 and value>1:
                                     result+=(value-1)*2 
                                 elif value>1:
                                      result+=value*2
                     else:
                         for key,value in hash_mirror.items():
                                 if value%2 and value>1:
                                     result+=(value-1)*2 
                                 elif value>1:
                                      result+=value*2                        
        if hash_reverse:
           for key,value in hash_reverse.items():
               rev=key[::-1]
               if key in temp and rev in temp :
                  result+=min(value[0],hash_reverse[rev][0])*4
                  del temp[key]
                  del temp[rev]
        return result 
Solution().longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"])
class TestApp:
      def testing_case_one(self):
          assert Solution().longestPalindrome(["cc","ll","gg"])==2 
      def testing_case_two(self):
          assert Solution().longestPalindrome(["ab","ty","yt","lc","cl","ab"])==8
      def testing_case_three(self):
          assert Solution().longestPalindrome(["lc","cl","gg"])==6
      def testing_case_four(self):
          assert Solution().longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"])==22
      def testing_case_five(self):
          assert Solution().longestPalindrome(["ga","ac","aa","ag","gc","cg","aa","ac","cg","ga","ga","gg","cg","ca","cg","gg","ca","ag","cc","ag","aa","cg","gg"])==34
