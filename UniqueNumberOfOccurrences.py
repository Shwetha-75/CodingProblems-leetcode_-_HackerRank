from collections import Counter
def uniqueNumber(nums):
    dict1=sorted(Counter(nums).items(),key= lambda x:x[1])
    for i in range(1,len(dict1)):
        if dict1[i-1][1]==dict1[i][1]:
            return False
    return True
nums=[1,2,2,3,3,3]
print(uniqueNumber(nums))