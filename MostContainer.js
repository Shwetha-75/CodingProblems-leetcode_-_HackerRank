let area=  (array) =>{
    let maxarea=0;
    //traversing thorugh n-1 elements
    for(i=0;i<array.length-1;i++)
    {
        //traversing thorugh n elements
        for( j=i+1;j<array.length;j++)
        {
            //calculating the area
            //area=min(array[i],array[j])*(j-i)
            temp=(array[i]<array[j]?array[i]:array[j])*(j-i)
            if(temp>maxarea)
            {
                //replacing the maxArea for every index
                maxarea=temp
            }
        }
    }
    return maxarea
}
array=[3,7,5,6,8,4]//21
console.log(area(array))