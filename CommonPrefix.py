class Solution(object):
    def longestCommonPrefix(self, strs):
        newString=""
        for index,element in enumerate(strs[0]):
            if self.iscommon(strs,index,element):newString+=element
            else:
                break
        return newString
    def iscommon(self,strs,index,element):
        for i in strs:
            
            if i[index]!=element or len(i)<=1:return False
        return True
strs=["ab","a"]
s=Solution()
print(s.longestCommonPrefix(strs))