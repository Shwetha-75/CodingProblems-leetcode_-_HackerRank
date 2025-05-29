#Here we have to remove only the matching adjacent element
# EG:1 we have string-->abba
#In 1st operation we remove bb --> both are adjacent
#resultant will be aa
#both are adjacent so we remove aa
# we obtain empty string
#EG:2 we have string-->aabba
#In 1st operation we obtain bba --> aa was adjacent elements
#In 2nd operation we obtain a--> bb was adjacent elements
#For this approach we have to use stack 
 
s="aabba"
stack=[]
#EG: 2 []-->empty stack
#iterating through strings aabba 
for i in s:
    #at i-->a and index 0 [] checking whether we have in stack are not-->False
    #at i-->a and index 1 [a] and at the top which means stack[-1] we have a so poping stack we obtain empty stack []
    #at i-->b and index 2 [] and checking the condition-->False
    #at i-->b and index 3 [b] and at the top which means stack[-1] we have b so poping out stack[-1]
    #at i-->a and index 4 [] and checking the condition-->False 
    if stack and stack[-1]==i:
        stack.pop()
    #at i-->a and index 0 appending a [a]-->False at index 0
    #at i-->b and index 2 appending b [b]-->False at index 2
    #at i-->a and index 4 appending a [a]-->False at index 4
    else:
        stack.append(i)
if len(stack)==0:
     print("Empty String")
else:
    print(stack)


    