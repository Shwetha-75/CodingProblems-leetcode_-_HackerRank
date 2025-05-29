function printFibonacci(n)
{
    if(n==0)
    {
        return 0
    }
    if(n==1)
    {
        return 1
    }
    prev=0
    cur=1
    count=1
    next=0
    console.log("0 \n1")
    while(count<n)
    {
        next=prev+cur
        prev=cur
        cur=next
        count++
        console.log(next.toString())
    }
    
}
printFibonacci(5)