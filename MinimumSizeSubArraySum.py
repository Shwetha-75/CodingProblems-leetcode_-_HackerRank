#Givne the array elements 
#[2,3,1,2,4,3] target=7
#  find the minimum subArray when we take the sum of all array elements it should be greater than or equal to target
#
#
#
import sys
#[2,3,1,2,4,3]      target=7
# 0 1 2 3 4 5 
# l=0 r=0, sum=0 m=max   l=0, r=1, sum=2, m=max   l=0,r=2,sum=5,m=max   l=0,r=3,m=max               l=1,r=4,m=4,sum=6           l=3,r=5,sum=6,m=3
# sum=2                          sum=2+3-->5         sum=1+5-->6          sum=6+2-->8                  sum=10                       sum=6+3=9
# 2>=7:False                     5>=7  False         6>=7 False            8>=7::True                  10>=7                        9>=7
#                                                                             m=min(m,r-l+1)           m=min(4,4)                   m=min(3,5-3+1)     
#                                                                             m=4                      m=4                          m=3
#                                                                             sum=8-2-->6               sum=10-3-->7                sum=9-2=7
#                                                                             l+=1-->1                  l+=1-->2                    l+=1-->4
#                                                                             6>=7::False               7>=7::True                  7>=7
#                                                                                                       m=min(4,4-2+1)              m=min(3,5-4+1)
#                                                                                                        m=3                        m=2
#                                                                                                        sum=7-1=6                  sum=7-4-->3
#                                                                                                        l+=1-->3                   l+=1-->4
def minimumSizeSubArraySum(nums,target):#                                                                                           3>=7
    left=sumMinimum=0
    minLen=sys.maxsize
    for i in range(len(nums)):
        #keep on adding every possible element in sequence
        sumMinimum+=nums[i]
        #iterate until sumMinimum is greater than target
        while sumMinimum>=target:
            #take the minimum among prevoius len of subarray and current len of subarray
            minLen=min(minLen,i-left+1)
            #update sumMinimum to remove the left index element so that we can 
            #consider sum of next subarray
            #
            #  
            #
            #
            sumMinimum-=nums[left]
            #changing left pointer
            left+=1
    return minLen if minLen!=sys.maxsize else 0#observation if the trget is not found

nums=[2,3,1,2,4,3]
target=7
print(minimumSizeSubArraySum(nums,target))