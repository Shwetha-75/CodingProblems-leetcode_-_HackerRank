const resultArray=(array,target)=>
{
  //creating map
   obj={}
   //dynamic array
   
   //traversing through array elements
   for(i=0;i<array.length;i++)
   {
    //calculating the target
      temp=target-array[i]
      //checking whether the required elements suppose
      //target --> 7 array[i]-->4 suntracting both we get 3 if 3 is present in obj as key then
      //we can get the index of 3 as for key-value we stored like element-index
      if(temp in obj)
      {
        return [obj[temp],i]
      }
      else
      {
        //if it is not present means we will be storing the in obj
        obj[array[i]]=i
      }
   }
   console.log(obj)
   return []
}
array=[5,4,3,2]
target=7
console.log(resultArray(array,target))