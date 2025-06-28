#Leet code day 16-04-2024 problem

'''
Question: Given array elements such that counte the number of unique element 
left out after removal of k elements
'''

from collections import Counter 
def leastCount(nums,k=3):
    #using counter class to count the frequencies of array elements and sorte according to frequencies 
    #in ascending order
    #Step: 1
    dict1=dict(sorted(Counter(nums).items(),key= lambda x:x[1]))
    #mistake
    #list1=list(dict1)
    #corrected 
    #Step 2
    #list1=[v for i,v in dict1.items() ]
    #storing the list elements according to the sorted order of values 
    list1=[]
    
   
    for i in dict1:
        temp=dict1[i] 
        #appending the elements according to their frequencies
        while temp!=0:
            list1.append(i)
            temp-=1
    #removing the k elements
    
    for i in  range(k): dict1[list1[i]]-=1
   
    
    #counting the left out unique elements
    result=list(dict1.items())
    count=len([result[i][0]  for i in range(len(result)) if result[i][1]>=1])
    
    '''for i in dict1:
        if dict1[i]>=1:
           count+=1'''
    print(count)
   
    
nums=[2,1,1,3,3,3]
leastCount(nums)