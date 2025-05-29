function selectionSort(array)
{
    n=array.length
    //outer loop
    for(i=0;i<n;i++)
    {
        min=array[i]
        index=i
        //inner loop
        for(j=i+1;j<n;j++)
        {
            if(array[j]<min)
            {
                min=array[j]
                index=j 
            }
            
        }
        //swapping
        temp=array[i]
        array[i]=min 
        array[index]=temp
    }
    return array 

}
array=[2,5,8,1,0,8]
console.log(selectionSort(array))