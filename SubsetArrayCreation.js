const result=function(array)
{
    arr=[]
    function helper(array,i,subset)
    {
        if(i==array.length)
        {
            arr.push(subset.slice())
            return
        }
        helper(array,i+1,subset)
        subset.push(array[i])
        helper(array,i+1,subset)
        subset.pop()
    }
    helper(array,0,[])
    return arr
}

array=[]
console.log(result(array))