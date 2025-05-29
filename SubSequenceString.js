const result=(str1,str2)=>
{
    index_str1=0
    index_str2=0
    //observations 
    //observation-->1
    if(str1.length==0) return true
    //observation-->2
    if(str1.length>str2.length) return false
    //Stopping condition
    while(index_str1<str1.length && index_str2<str2.length)
    {
        //checking for the character 
        if(str1[index_str1]==str2[index_str2])
        {
            //if the character sequence if found incrementing the value
            index_str1++
        }
        //incrementing iteration for str2
        index_str2++
    }
    return str1.length==index_str1
}
str1=""
str2="adgdc"
console.log(result(str1,str2))