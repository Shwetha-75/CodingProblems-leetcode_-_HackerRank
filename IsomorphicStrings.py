class IsomorphicStrings:
    def isomorphicString(str1,str2):
        dict1={}
        dict2={}
        if len(str1)!=len(str2):return False
        for char_1,char_2 in zip(str1,str2):
            if char_1 in dict1:
                if dict1[char_1]!=char_2:
                    return False
            else:
                dict1[char_1]=char_2
            if char_2 in dict2:
                if dict2[char_2]!=char_1:
                    return False
            else:
                dict1[char_2]=char_1
        return True
str1="abba"
str2="pqq"
print(IsomorphicStrings.isomorphicString(str1,str2))