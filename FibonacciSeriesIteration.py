class FibonacciSeries:
    def fibonacci(n):
        if n==0: return 0
        if n==1: return 1
        prev=0
        current=1
        count=1
        #f(n)
        while count<n:
            next=prev+current
            prev=current
            current=next
            count+=1
        return next
n=6
print(FibonacciSeries.fibonacci(n))