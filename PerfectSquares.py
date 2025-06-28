import math
def perfectSquare(num):
    if num==1 or num==0:  
        print("Perfect Square")
        return 
    #taking the sqrt of that number
    div=int(math.sqrt(num))
    ##checking the if the div * div is equal to the num
    if num==div*div:
        print("Perfect Square")
    else:
        print("Not a perfect square")
perfectSquare(14)