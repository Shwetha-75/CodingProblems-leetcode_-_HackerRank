const result=(array,target)=>
{
    left=0
    right=array.length-1
    // stopping condition
    while(left<=right)
    {
        mid=Math.floor((left+right)/2)
        // #if the target is present in mid value or not
        if(target===array[mid])
        {
            return mid;
        }
        // #checking if the left part is sorted 
        // #if the left part is sorted the exploring the left part
        else if(array[left]<=array[mid])
        {
            // checking if the target is ranging between the array[left]<=target<=array[mid]
            // #explore left part
            if(target>=array[left] && target<=array[mid])
            {
                right=mid-1
            }
            // if it is not ranging i have to explore right part
            else{
                left=mid+1
            }
        }
        else
        {// right part is sorted
            //if the target is ranging between ---> array[mid]<=target<=array[right]
            if(target>=array[mid] && target<=array[right])
            {
                left=mid+1
            }
            else//target is mid=ght be ranging 
            {
                right=mid-1
            }
        }
    }
    return -1
}
array=[4,5,6,7,0,1,2]
target=6

console.log(result(array,target))