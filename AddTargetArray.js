const listArray=(array,target)=>
{
    listIndices=[]
    for(i=0;i<array.length-1;i++)
    {
        for(j=i+1;j<array.length;j++)
        {
            if(array[i]+array[j]==target)
            {
                listIndices.push(i)
                listIndices.push(j)
                return listIndices
            }
        }
    }
    return listIndices
}
array=[5,4,3,2]
target=7
console.log(listArray(array,target))