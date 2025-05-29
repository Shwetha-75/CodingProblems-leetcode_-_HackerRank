def validCheck(string):
    # we are storing the pairs of parenthesis as key-value pair in hash map
    dict1={")":"(","}":"{","]":"["}
    #creating list-->dynamic array, to perform like stack
    stack=[]
    #y=terating through string
    for i in string:
        #checking element is present in dict1
        if i in dict1:
            #if in stack and in the top of the stack we have value of key
            #["(","}","("]
            #value="(" and key is ")" i.e, dict1[")"]---->"(" 
            if stack and stack[-1]==dict1[i]:
                #removing the last element
                #by defualt it will removes the last element
                stack.pop()
            else:
                False
        else:
            #if it is not
            stack.append(i)
    return not  stack
print(validCheck(")(){\\}"))