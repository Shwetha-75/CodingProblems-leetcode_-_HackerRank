const result=function fibonacci(n)
{
    if(n==0)
    {
        return 0
    }
    if(n==1)
    {
        return 1
    }
    fibo=fibonacci(n-1)+fibonacci(n-2)
    return fibo
}

n=6
console.log(result(n))