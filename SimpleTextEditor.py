testCases=int(input())
stack=[]#stack
string=''#create empty string
#number of test cases
for i in range(testCases):
    #operation to be performed listed out
    operation=list(input().split())
    #performing the operation according to the user specified
    match int(operation[0]):
        #to append
        case 1: 
            stack.append(string)#first store all the string object onto stack after each operation
            #Only at append and delete we will be keep on tracking all the changes 
            string+=operation[1]
            #to delete
        case 2: 
            stack.append(string)
            string=string[:len(string)-int(operation[1])]#deleteing the last number of characters
            #to print
        case 3: 
             print(string[int(operation[1])-1])#printing the characters at specified index
             #undo
        case 4:
            string=stack.pop()#storing the last changes in string 
