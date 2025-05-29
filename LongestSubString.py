def longest(string):
    #final substring
    substring=""
    #outer loop to iterate over the string
    for i in range(len(string)):
        temp=""#to hold the unique substring at i the iteration
        #inner loop to itarate over the next character
        #suppose we have javaisfun 
        #j       a     v           a                 i        s      f       u    n
        #ja      av    va          ai                is       sf     fu      un
        #jav           vai         ais               isf      sfu    fun
        #              vais        aisf              isfu     sfun
        #              vaisf       aisfu             isfun
        #              vaisfu      aisfun
        #              vaisfun
        for j in range(i,len(string)):
            #to check character is repeated 
            if string[j] not in temp:
                temp+=string[j]
            else:
                break
        #to replace it with max substring
        if len(substring)<len(temp):
            substring=temp
    return substring
string="tmmzuxt"
print(longest(string))
        
        
        
        
        
        
        
        
        
        
        
        
        
        