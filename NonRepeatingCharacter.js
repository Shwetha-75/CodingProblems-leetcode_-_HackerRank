const result=(string)=>
{
   //traversing through each character in the string
    for(i=0;i<string.length;i++)
    {
        let repeat=false
        //traversing through each characters in the string
        for(j=0;j<string.length;j++)
        {
            //checking the repeating character
            if(string[i]===string[j] && i!=j)
            {
                repeat=true
            }
        }
        if(repeat===false)
        {
            return i
        }
    }
    return null
}
string="abbaaggnnj"
console.log(result(string))
//console.log(string.length)