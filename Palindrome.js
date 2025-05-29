const result=(string)=>
{
    temp=""
    for(i=string.length-1;i>=0;i--)
    {
        temp+=string[i]
    }
    if(temp===string)
    {
        return true
    }
    else
    {
        return false
    }
}
string="abba"
console.log(result(string))