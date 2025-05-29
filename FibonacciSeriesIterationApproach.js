const result=(n)=>
{               //    0,1,2,3,4,5,6,7...... 
    if(n==0)//        0,1,1,2,3,5,8,13...                              f(1)-->1
    {//               P,C N,                                           f(0)-->0
        return 0//      P,C,N                                          F(n)=F(n-1)+F(n-2)
    }//                                                                F(3)=F(2)+F(1)-->1+1-->2
    if(n==1)//                                                         F(2)=F(1)+F(0)-->1
    {//
        return 1//
    }//

    prev=0
    cur=1
    count=1
    next=0
    while(count<n)
    {
        next=prev+cur
        prev=cur
        cur=next
        count++

    }
    return next

}
n=2
console.log(result(n))