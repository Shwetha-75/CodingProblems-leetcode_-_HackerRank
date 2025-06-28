def palindrome(string):
    if len(string)==1: return True
    temp=string[-1:-len(string)-1:-1]
    if temp==string:
        return True
    else:
        return False
print(palindrome("a"))