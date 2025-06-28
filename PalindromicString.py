#Let me start with the brute force approach
#The problem is to check every character in the string and take the subastring 
#and check wether they are plindrome or not 
#Given string is non empty string 
#TestCase: 1                                         TestCase 2 
#  abc                                                 aaa
#  a     b     c                                       a           a     a
#  ab    bc                                            aa          aa
#  abc                                                 aaa
# among these there are 3                              all are palindrome
# each single character is a palindrome                if the given string is palidrome 
#                                                      dont take factorial it won't work
def palindromeCheckCount(string):
    count=0
    for i in range(len(string)):
        for j in range(i,len(string)):
            sub=string[i:j+1:]
            if sub==sub[::-1]:
                count+=1
    print(count)
palindromeCheckCount("abccba")