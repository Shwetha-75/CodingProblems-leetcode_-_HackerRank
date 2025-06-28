function duplicate(array)
{

    for(let i=0;i<array.length;i++)
    {
        let count=1
        for(let j=i+1;j<array.length;j++)
        {
            if(array[i]==array[j])
            {
                count++;
            }
        }
        if(count>=2)
        {
            return array[i];
        }
        
    }
}
array=[1,2,3,4,6,6,5]
console.log(duplicate(array))