import math
def percentage(word,letter):
    #count function is used for every sequence datatype
    countLetter=word.count(letter)
    per=math.floor((countLetter/len(string))*100)
    
    print(per)
string="foobar"
percentage(string,'o')