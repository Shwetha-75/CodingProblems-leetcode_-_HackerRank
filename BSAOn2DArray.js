function binarySearch(array,target)
{
    let rows=array.length
    let col=array[0].length
    let top=0
    let bottom=rows-1
    let left=0
    let right=col-1
    // #We observations 
//  1. if the array is empty
    if(array.length==0)
    {
        return False
    }
    // 2. if we have only one element
    if(array[0].length==1)
    {
        if(target==array[0][0])
        {
            return true
        }
        else{
            return false
        }
    }
    //3. if we have the target greater than the maximum
    if(target>array[rows-1][col-1])
    {
        return false
    }
    let mid=0
    //target row to find the element 
    while(top<=bottom)
    {
        mid=Math.floor((top+bottom)/2)
        // #if target is lesser than the middle row first element 
        if(target<array[mid][0])
        {
            bottom=mid-1
        }
        //if the target is greater than the middle roe last element
        else if(target>array[mid][col-1])
        {
            top=mid+1
        }
        // because if the bot the condition fails means the target is the same row itself
        else{
            break;
        }
    }
    // # we are performing BSA on particular row
    let middle=0
    while(left<=right)
    {
        middle=Math.floor((left+right)/2)
        if(target==array[mid][middle])
        {
            return true
        }
        else if(target>array[mid][middle])
        {
            left=middle+1
        }
        else
        {
            right=middle-1
        }
    }
    return false

}
array=[[1,2,3],[4,5,6],[7,8,9]]
target=7
console.log(binarySearch(array,target))