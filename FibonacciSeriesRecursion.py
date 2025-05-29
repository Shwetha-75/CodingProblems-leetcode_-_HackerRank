class FibonacciSeries:
    def findFibonacci(n):
        if n==0: return 0
        if n==1: return 1
        result=FibonacciSeries.findFibonacci(n-1)+FibonacciSeries.findFibonacci(n-2)
        return result
n=5
print(FibonacciSeries.findFibonacci(n))

        