class RemoveDuplicate:
    #removing the duplicates
    def removingDuplicate(self,string):
        newString=string[0]
        for i in range(1,len(string)):
            #checking consecutive character is repeated or not
            if string[i-1]!=string[i]:
                newString+=string[i]
        return newString
remove=RemoveDuplicate()
string=input("Enter the String: ")
print(remove.removingDuplicate(string))
