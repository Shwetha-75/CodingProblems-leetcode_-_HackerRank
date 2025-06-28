def isSubSequence(str1,str2):
    if len(str1)==0: return True
    if len(str1)>len(str2): return False
    index_str1,index_str2=0,0
    while index_str1<len(str1) and index_str2<len(str2):
           index_str2,index_str1=index_str2+1,index_str1+(str1[index_str1]==str2[index_str2])
    return len(str1)==index_str1
str1="fgh"
str2="fgh"
print(isSubSequence(str1,str2))