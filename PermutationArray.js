const result= (array)=>
{
    let permutation=[]
    if(array.length==0)
    {
        permutation.push(array.slice())
        return permutation
    }
    function permutationsPerformance(array,i)
    {
        //pushing the array elements
        if(i===array.length-1)
        {
            permutation.push(array.slice())
        }
        for (let j=i;j<array.length;j++)
        {
            //swap
            let temp=array[j]
            array[j]=array[i]
            array[i]=temp
        
            //recursive call
            permutationsPerformance(array,i+1)
            //swap
            let temp1=array[j]
            array[j]=array[i]
            array[i]=temp1
            
        }
    }
    permutationsPerformance(array,0)
    return permutation
}
array=[1,2,3]
console.log(result(array))