from collections import Counter
#Majority ELement
#This approach is simsilar to Boyer-Moore Alogorithm
def majoriyElement(nums,k=3):
    #result=[]
    result=[]
    #dict1 too hold the the key as list elements as value as their frequencies
    # or else we can use Counter Class from collections
    dict1=Counter(nums)
    
    #find the majority elemenst whic satisfies the threshold
    for i in dict1:
        if dict1[i]>len(nums)//k:#n/k here k--->3
            result.append(i)
    print(result) 
nums=[3,2,3]
majoriyElement(nums)