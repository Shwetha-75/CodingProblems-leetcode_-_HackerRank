let status= function(array)
{
    if(array.length==0)
    {
        return True
    }
    first=array[0]
    last=array[array.length-1]
    if(first>last)
    {
        for(i=0;i<array.length-1;i++)
        {
            if(!(array[i]>array[i+1]))
            {
                return false
            }
        }
    }
    else if(first<last)
    {
        for(i=0;i<array.length-1;i++)
        {
            if(!(array[i]<array[i+1]))
            {
                return false
            }
        }
    }
    return true
}
array=[5,4,-1,2,1]
console.log(status(array))