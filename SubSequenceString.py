def SubSequenceString(s,t):
    #to track the length of the string s as well as to get indexes of string s
    count=0
    #traversing through each characters in string t
    for i in range(len(t)):
        #stopping condition 
        if count<len(s):
            #checking the character 
            if s[count]==t[i]:
                #incrementing the counter variable
                count+=1
        #if counter is same as length of the string s
        if count==len(s):
            return True
    return False
s="abc"
t="addgcabc"
print(SubSequenceString(s,t))
