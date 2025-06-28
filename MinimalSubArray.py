#Incomplete.....
import sys
array=[12,28,83,4,25,26,25,2,25,25,25,12]
target=213
result=[]
def helper(array,i,subset):
    if i==len(array):
        result.append(subset[::])
        return 
    helper(array,i+1,subset)
    subset.append(array[i])
    helper(array,i+1,subset)
    subset.pop()
i=0
su=[]
min=sys.maxsize
helper(array,i,[])
for i in result:
    if sum(i)>=target:
        if len(i)<min:
            min=len(i)
            su=i
print(su)


           


