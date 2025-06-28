'''


Given a sorted integer array nums and an integer n, add/patch elements to the array 
such that any number in the range [1, n] inclusive can be formed by 
the sum of some elements in the array.

Return the minimum number of patches required.


Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1


'''


# The problem statement clearly states that we have to count number of patches that can be 
# addedd into the current array so that taking the sum each subset it as to form between the 
# range from 1 to n 
# 
# For Example 1: nums=[1,2,2]  n=5
#               [1],[2],[2],[1,2],[2,2],[1,2,2]
#                1,  2   2   3     4      5      is in the range from 1 to n
# 
#               so conclusion number of patech are 0
# For Example 2: nums=[1,5,10]  n = 20 
#                [1],[5],[10],[1,5],[1,10],[5,10],[1,5,10]
#                 1,  5 ,10  ,  6 ,  11,  15,     16    is not satisfying [1,20]
            #    --------------False Assumption since the struture modification is not allowed 
#                  include 2
#                the sum elements will be 1,2,3,5,7,8,10,12,13,17,18  is not satisfying [1,20]
# 
#                    include 4 since 3 is there 
#               the sum elements will be  1,2,3,4,5,...............num[nums.length] >=n 
# 


# Best Approach is to have to follow Greedy Approach 
# 
# Step 1: To Count the number of patches to be included to make the condition satisfied. 
#          and We have to make note of sum of the elements from index 0 till the last element 
# Step 2: Make a note of indices intialize it ot zero 
# Setp 3: for element it as to be less than or equal to sum (till now what we have included)
# Step 4: if the above condition satisfies than add up the sum and incremnt the index value i
# Step 5: if the condition fails than double the sum and increment the number of patches  
# Step 6: return the number of patches



class Solution:
    def patcharraay(self,array:list,n:int):
        
        # step 1
        sum=1
        patches=0
        length=len(array)
        # step 2
        index=0
        # Step 3
        while sum<=n:
            # step 4
              if index<length and array[index]<=sum:
                  sum+=array[index]
                  index+=1
            # step 5
              else:
                  sum+=sum
                  patches+=1
        # step 6
        return patches 
    
def main():
    sol=Solution()
    result=sol.patcharraay([1,5,10],20)
    print(result)
main()