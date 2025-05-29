def palindromeIndex(string):
    left=0
    right=len(string)-1
    while left<right:
        if string[left]!=string[right]:
            if ispalindrome(string,left+1,right):
                return right
            else:
                return left
        left+=1
        right-=1
    return -1
def ispalindrome(string,left,right):
    while left<right:
        if string[left]==string[right]:
            return False
        left+=1
        right-=1
    return True
string="aaab"
print(palindromeIndex(string))