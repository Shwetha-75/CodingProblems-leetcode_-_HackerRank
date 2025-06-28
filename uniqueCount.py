def uniqueCount(string):
    dict1={}
    for i in string:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    for i in dict1:
        if dict1[i]==1:
            return string.index(i)
    return -1
print(uniqueCount("leetcode"))