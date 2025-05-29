
function result(array)
{
    function merge(array1,array2)
   {
    //console.log(array1)
    //console.log(array2)
    //resultant array
    let resultant=[]
    //index to iterate over array1 elements
    i=0
    //index to iterate over array2 elements
    j=0
    //merging the two array elements
    while(i<array1.length && j<array2.length)
    {
        //checking condition to push the array elements in sorted order
        //to maintain the intial ordering of the array elements
        if(array1[i]<=array2[j])
        {
            resultant.push(array1[i])
            i++;
        }
        else
        {
            resultant.push(array2[j])
            j++;
        }

    }

    //such cases where array1.length is greater than array2.length
    while(i<array1.length)
    {
        resultant.push(array1[i])
        i++;
    }

    //such cases where array2.length is greater than array1.length

    while(j<array2.length)
    {
        resultant.push(array2[j])
        j++;
    }
    //console.log(resultant)
    return resultant

}

    if(array.length<=1)
    {
        return array.slice()
    }
    let  middle=Math.floor(array.length/2)

    //left side recursive call
    let leftside=result(array.slice(0,middle))
    //rightside recursive call
    let rightside=result(array.slice(middle))
    //calling the function to merge arary elements

    return merge(leftside,rightside)

}

array=[5,6,2,1,9]

console.log(result(array))
//mistakes 

//define all the variables using let keyword dont commit the mistakes again