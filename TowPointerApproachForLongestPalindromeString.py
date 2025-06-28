def longestPalidrome(string):
    #observations
    if len(string)==0:
        return ""
    if len(string)==1:
        return string
    if string==string[::-1]:#if the string itself is a palindrome
        return string
    maxLen=0
    substring=""
    for i in range(len(string)):
        #odd length substring
        left=right=i
        while left>=0 and right<len(string) and string[left]==string[right]:
              if (right-left)+1>maxLen:
                  substring=string[left:right+1]
                  maxLen=(right-left)+1
              left-=1
              right+=1
        #even length
        left=i
        right=i+1
        while left>=0 and right<len(string) and string[left]==string[right]:
            if(right-left)+1>maxLen:
                substring=string[left:right+1]
                maxLen=(right-left)+1
            left-=1
            right+=1
    return substring
print(longestPalidrome("baabad"))#baab
#                          s--->    b a a b a d m=0 sub="" n=6       even length l=i, r=i+1
#O: i=0       odd length                                      O: l=0,r=1
#                                          
#  left=0 right=0
# I: left>=0 and right<n and s[0]==s[0]:                       I: l>=0 and r<n  and s[0]==s[1]--->false
#     True                                                    O: i=1 
#                                                           #       I: l=1, r=2
#        if 0-0+1>m                                                     l>=0 and r<n and s[1]==s[2]-->True
#             1>0--> True                                                   r-l+1>m-->2-1+1>1
#                                                                             m=2
#             sub=b  ,m=1                                                       sub=aa
#    left=-1, right=1                                                        l=0,r=3
#                                                                        l>=0 and r<n and s[0]==s[3]-->True
# 
# O: i=1                                                                        m=4
#    left=1, right=1                                                            sub=baab
#     I: 1>=0 and 1<n and s[1]==s[1]:
#        
#  -->conclusion in odd length always 
#   for i iteration first time the condition holds 
#
#
#
#
#
#
#
#
#