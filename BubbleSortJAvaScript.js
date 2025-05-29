const result=(array)=>
{
    n=array.length
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1;j++)
        {
            //swapping
            if(array[j]>array[j+1])
            {
               temp=array[j]
               array[j]=array[j+1]
               array[j+1]=temp
            }
        }
    }
    return array
}
array=[4,6,2,1,8,9]
console.log(result(array))