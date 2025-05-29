#brutforce approach
def longest(string):
    maxLen=1
    result=""
    
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            sub=string[i:j+1]
            if sub==sub[::-1]:
                if len(sub)>maxLen:
                    maxLen=max(len(sub),maxLen)
                    result=sub
    print(result)
longest("aacabdkacaa")
#for each substrung palindrome is checked
#a                       #a
#aa                       ac 
#aac                      aca
#aaca                     acab
#aacab                    acabd
#aacabd                   acabdk
#aacabdk                  acabdka
#aacabdka                 acabdkac
##aacabdkac               .......
##aacabdkaca               maxLen=3
##aacabdkacaa              substring=aca
#maxLen=2
#substring=aa