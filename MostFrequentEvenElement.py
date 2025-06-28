from collections import Counter
def frequentEven(nums):
    #filtering the even numbers among them and sorting accoring to
    nums=sorted([i for i in nums if i%2==0],reverse=True)
    
    #if the list is empty
    if len(nums)==0:
        #print -1 whicch no eveen elements
        print(-1)
    else:
        #{2:}
        print(max(Counter(nums),key=(Counter(nums).get)))
    
nums=[1,4,4,5,2,2,2,2,8,8,8,8,8,7,6,6,9,9,9,9]
frequentEven(nums)