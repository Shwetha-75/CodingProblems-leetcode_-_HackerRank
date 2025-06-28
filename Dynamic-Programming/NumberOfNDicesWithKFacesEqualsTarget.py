from itertools import product
def helper(n:int,k:int):
    result=[list(range(1,n+1)) for _ in range(k+1)]
    result=list(product(*result))
    print(result)
helper(30,30)