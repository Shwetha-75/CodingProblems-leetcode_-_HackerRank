function groupAnagrams(string)
{
    list1=[]
    for(i=0;i<string.length;i++)
    {
        list1.push(string[i].split("").sort().join(""))
    }
    obj={}
    for(i=0;i<string.length;i++)
    {
        if(list1[i] in obj)
        {
            obj[list1[i]].push(string[i])
            
        } 
        else
        {
            obj[list1[i]]=[string[i]]

        }

    }
    result=[]
    for(i in obj)
    {
        result.push(obj[i])
    }
    console.log(result)
}
string=["silent","listen","peacock"]
groupAnagrams(string)