class HappyNumber:
    def isHappyNumber(n):
        visit=set()
        while n not in visit:
            visit.add(n)
            n=HappyNumber.square(n)
            if n==1:
                return True
        return False
    
    def square(n):
        sum=0
        while n!=0:
            rem=int(n%10)
            sum+=rem**2
            n=int(n/10)
        return sum
n=int(input("Enter the Number"))
print(HappyNumber.isHappyNumber(n))