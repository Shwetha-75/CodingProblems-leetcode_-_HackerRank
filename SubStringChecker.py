class SubStringCheck:
    def checkSubString():
        #user input
        str1=input()
        #str=abab
        #temp=ababababa
        temp=str1+str1
        #removing first letter
        #temp=babababa
        
        temp=temp.removeprefix(temp[0])
        #removing last letter
        #temp=bababab
        temp=temp.removesuffix(temp[len(temp)-1])
        #if ababa in bababab
        if str1 in temp:
            return True
        else:
            return False
print(SubStringCheck.checkSubString())