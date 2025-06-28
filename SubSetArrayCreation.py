class Solution(object):
 def isCreatingSubset(self,array):
    result=[]
    #creating subset 
    subset=[]
    #function to call recursively to creat subset
    def helper(i,array,subset):
       #checking if it has reached the last element
       if i==len(array):
          #adding to the result set
          result.append(subset[::])
          
          return
       #calling the function recursively without add
       helper(i+1,array,subset)
       #after adding to the subset
       subset.append(array[i])
       #calling the function recursively
       helper(i+1,array,subset)
       #poping out the element
       subset.pop()
    subset=[]
    #function call
    helper(0,array,subset)
    return result
array=[1,2,3]
s=Solution()
print(s.isCreatingSubset(array))
