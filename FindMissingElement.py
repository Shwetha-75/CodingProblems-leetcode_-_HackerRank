#given=[1,2,3,5]
#missing array element=4
def findMissing(nums):
    array=[0]*(len(nums)+1)
    print(array)
    for i in nums:
        array[i-1]=1
    print(array)
    for i in range(len(array)):
        if array[i]==0:
            return i+1
nums=[1,2,3,5]
print(findMissing(nums))