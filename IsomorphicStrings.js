let status=(s,t)=>
{
    object_s={}
    object_t={}
    if(s.length!=t.length)
    {
        return false
    }
    for(i=0;i<s.length;i++)
    {
        if(s[i] in object_s)
        {
            if(object_s[s[i]]!=t[i])
            {
                return false
            }
        }
        else
        {
            object_s[s[i]]=t[i]
        }

        if(t[i] in object_t)
        {
            if(object_t[t[i]]!=s[i])
            {
                return false
            }
        }
        else
        {
            object_t[t[i]]=s[i]
        }
    }
    return true

}
s="abba"
t="pqrp"
console.log(status(s,t))