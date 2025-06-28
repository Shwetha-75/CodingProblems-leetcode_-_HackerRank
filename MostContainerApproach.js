const area=(array)=>
{
    //max Area
    maxArea=0
    //left pointer
    left=0
    //right pointer
    right=array.length-1
    while(left<right)
    {
        //area=min(array[left],array[right])*(j-1)
        height=Math.min(array[left],array[right])
        width=right-left
        //max Area 
        maxArea=Math.max(maxArea,height*width)
        //shifting the pointers
        if(array[left]<array[right]) left+=1
        else right-=1

    }
    return maxArea
}
array=[3,7,5,6,8,4]
console.log(area(array))