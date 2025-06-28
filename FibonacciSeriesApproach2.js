 let obj={0:0,1:1}
function fibonacciSeries(n)
{
    if(n in obj)
    {
        return obj[n]
    }
    else
    {
        obj[n]=fibonacciSeries(n-1)+fibonacciSeries(n-2)
        return obj[n]
    }
}
n=5
console.log(fibonacciSeries(n))