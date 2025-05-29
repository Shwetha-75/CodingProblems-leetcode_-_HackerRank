def longest(nums):
    nums=sorted(nums)
    longCount=1
    count=1
    for i in range(1,len(nums)):
        #one mistake we have consider in such cases where repeated will also be there
        #we should not consider the repeated elements in the count
        #current element is not equal to the previous element
        if nums[i]!=nums[i-1]:
            #checking the sequence count
                if nums[i-1]+1==nums[i]:
                    count+=1
                else:
                    #taking maximum among them
                    longCount=max(longCount,count)
                    count=1
    print(max(longCount,count))
   
nums=[100,4,200,1,3,2]
longest(nums)