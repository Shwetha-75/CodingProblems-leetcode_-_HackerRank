def palindromicString(string):
    left=0
    right=len(string)-1
    while left<right:
        if string[left]==string[right]:
            left+=1
            right-=1
        else:
            temp=string[left+1::]
            if temp==temp[::-1]: return left
            temp=string[left:right:] 
            if temp==temp[::-1]: return right
            return -1 
print(palindromicString("aaabaaac"))
        
        