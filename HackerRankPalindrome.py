#class declaration
class Check:
    #method to check whether the string is palindrome or not
   def ispalindrome(str1,left,right):
    #left poiunter and right pointer
    while left<right:
      if str1[left]!=str1[right]:
          return False
      left+=1
      right-=1
    #returning if it is palindrome
    return True
   #finding the index to remove the character to make it palindrome
   def findIndex():  
     str1=input()
     #left pointer
     left=0
     #right pointer
     right=len(str1)-1
     index=-1
     #looping to check the index 
     while left<right:
      if str1[left]!=str1[right]:
        #passing the substring as argument excluding the character to check the index of the character 
        if Check.ispalindrome(str1,left+1,right):
            return left
        else:
            return right
      left+=1
      right-=1
     return index
print(Check.findIndex()) 
