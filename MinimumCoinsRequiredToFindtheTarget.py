#Problem -Given a set of coin(array elements). find the minimum number of coins needed to make certain 
#amount of change
#target is 47

def greedyApproach(nums,target):
    #If the target is to find the minimum the sort the array elements in descending
    nums.sort(reverse=True)
    #set of minimum coins that required to make a certain change
    result=[]
    count=0
    remaining_amt=target
    #traversing through array elements
    for i in nums:
         #iterating through until the remaining amt <=array[i]
        while remaining_amt>=i:
            count+=1
            result.append(i)
            remaining_amt-=i
    if remaining_amt!=0:
        return -1
    else:
        return result
nums=[150]
target=76
if greedyApproach(nums,target)==-1:
    print("Not possible with the given denominations ")
else:
    print(greedyApproach(nums,target))
 