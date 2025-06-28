var filter=function(arr,fn)
{
    fn=function removegreaterThan10(n)
    {
        return n>10
    }
    fn=function firstIndex(n,i)
    {
        return i===0
    }
    fn=function addElements(n)
    {
        return n+1
    }

}
array=[0,10,20,30,40]
filter(arr,)