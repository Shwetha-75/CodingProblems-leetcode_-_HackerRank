const result=(string)=>
{
    map={}
    for(i=0;i<string.length;i++)
    {
        if(string[i] in map)
        {
            map[string[i]]++;
        }
        else
        {
            map[string[i]]=1
        }
    }
    console.log(map)//{ b: 1, a: 3, n: 3 }
    for(i =0;i<string.length;i++)
    {
        if(map[string[i]]==1)
        {
           
            return i
        }
    }
    return null;
}
string="banannab123@@#321"
console.log(result(string))