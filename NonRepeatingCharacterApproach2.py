def nonrepeatingCharacter(string):
    #enumerate function returns both index as well as element
    for i,element in enumerate(string):
        #counting the occurrences of each character
        if string.count(element)==1:
            #returning the index value
            return i
    return None

print(nonrepeatingCharacter("aaab48bgghh1122348ADF3tt"))
    