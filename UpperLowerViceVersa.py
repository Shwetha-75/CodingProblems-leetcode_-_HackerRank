class Conversion:
    def convertingMethod(string):
        newString=''
        for i in range(len(string)):
            #checking if it lower case
            if string[i].islower():
                #converting it to upper case
                newString+=string[i].upper()
            else:
                #converting it to lower case
                newString+=string[i].lower()
        return newString
#user input string value
string=input("Enter the string: ")
#printing the string before manipulation
print("Before conversion: ",string)
#calling the method to convert lower case to upper case or vice versa

print("After conversion: ",Conversion.convertingMethod(string))