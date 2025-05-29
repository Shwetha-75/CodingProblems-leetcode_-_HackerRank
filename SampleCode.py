def nonRepeatingCharacterIndex(string):
    dict1={}
    for i in string:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
   
    for index,element in enumerate(string):
        if dict1[element]==1:
            return index
    return None
string="bannanabj"
print(nonRepeatingCharacterIndex(string))
   