import math
def maximum(nums,k):
    
    while k!=0:
        temp=max(nums)
        nums.remove(temp)
        nums.append(temp-(math.floor(temp/2)))
        k-=1
    print(sum(nums))
        
nums=[5,4,9]
maximum(nums,2)  