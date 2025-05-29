const area=(array)=>
{
    maxarea=0
    //traversing through n-1 array elements
    for(i=0;i<array.length-1;i++)
    {
        //traversing through array upto n elements
        for(j=i+1;j<array.length;j++)
        {
            //finding the width
            const width=Math.min(array[i],array[j])
            //finding the height
            const height=j-i
            maxarea=Math.max(maxarea,height*width)
        }
    }
    return maxarea
}
array=[3,7,5,6,8,4]
console.log(area(array))