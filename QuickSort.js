function swap(array,i,j)
{
    let temp=array[i]
    array[i]=array[j]
    array[j]=temp
}

function partition(array,start=0,end=array.length-1)
{
    let middle=Math.floor((start+end)/2)
    swap(array,start,middle)

    let pivot=array[start]
    let i=start+1
    let j=end
    while(i<=j)
    {
        while(i<=array.length-1 && array[i]<pivot)
        {
            i++;
        }
        while(j>=0 && array[j]>pivot)
        {
            j--;
        }
        if(i<j)
        {
            swap(array,i,j)
        }

    }
    swap(array,start,j)
    return j

}

function quickSort(array,start=0,end=array.length-1)
{
    while(start<end)
    {
        let pivotIndex=partition(array,start,end)
        if(pivotIndex-start < end-pivotIndex)
        {
            quickSort(array,start,pivotIndex-1)
            start=pivotIndex+1
        }
        else
        {
            quickSort(array,pivotIndex+1,end)
            end=pivotIndex-1
        }
    }
    
}
array=[1,2,3,4,5,6,7]
quickSort(array)
console.log(array)