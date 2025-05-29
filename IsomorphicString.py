class Isomorphic:
    def checkIsomorphic(self,str1,str2):
        dict_s={}
        dict_t={}
        if len(str1)!=len(str2):
            return False
        for char_s,char_t in zip(str1,str2):
            if char_s in dict_s:
                if dict_s[char_s]!=char_t:
                    return False
            else:
                dict_s[char_s]=char_t
            if char_t in dict_t:
                if dict_t[char_t]!=char_s:
                    return False
            else:
                dict_t[char_t]=char_s
        return True
iso=Isomorphic()
print(iso.checkIsomorphic("abba","dog cat cat dog"))