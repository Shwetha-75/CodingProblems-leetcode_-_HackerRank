function radixSort(array)
{
    //maximum number
    const maxNumber=Math.max(...array)
    console.log(maxNumber)
    //numner of digits
    const number=Math.floor(Math.log10(maxNumber))+1

    for(let i=0;i<number;i++)
    {
        countingSort(array,i)
    }
    return array

}
function countingSort(array,place)
{
    const result=new Array(array.length).fill(0)
    console.log(result)
    const temp=new Array(10).fill(0)
    console.log(temp)
    //help full in taking digits place number
    const  divide=Math.pow(10,place)

    //frequencies
    for(let i of array)
    {
        //single digit from each i-->element
        let single=Math.floor(i/divide)%10
        temp[single]++;
    }

    //cummulative sum
    for(let i=1;i<10;i++)
    {
        temp[i]=temp[i-1]+temp[i]
    }

    //result array wuld be
    //in temp array the each elements -1 would be the index positon for result array 

    //reverse array
    for(let i=array.length-1;i>=0;i--)
    {
        console.log(array[i])
        let cur=Math.floor(array[i]/divide)%10
        temp[cur]--;
        result[temp[cur]]=array[i]
    }

    //copy from result to array

    for(let i=0;i<array.length;i++)
    {
        array[i]=result[i]
    }
   
}
const array=[284,71,67,90,32,1,65]
console.log(radixSort(array))