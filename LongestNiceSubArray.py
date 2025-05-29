def longestNiceSubArray(nums):
    left=0
    right=len(nums)-1
    def bitwise(array):
        ans=array[0]
        for i in range(1,len(array)):
            ans&=array[i]
            if ans!=0: return False
        return True
    maxLen=1   
    while left<right:
          
          if nums[left] & nums[right]==0:
            
            if bitwise(nums[left:right+1:]): 
                print(nums[left:right+1:])
                maxLen=max(maxLen,len(nums[left:right+1:]))
            else: right-=1 
          left+=1
             
    return maxLen
nums=[744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]
print(longestNiceSubArray(nums))