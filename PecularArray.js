function sumPower(array,power=1)
{
   sum=0
   for(i in array)
   {
      //checking if it is array or not 
       if(Array.isArray(array[i]))
       {
         //if it is array means calling recursively 
         //to get the sum of sub array
          sum+=sumPower(array[i],power+1)
          
       }
       else{
         //if it is not array if it in int element means adding the array elements
        sum+=array[i]
       }
   }
   return Math.pow(sum,power)

}
array=[1,2,3,[1,2]]
console.log(sumPower(array))