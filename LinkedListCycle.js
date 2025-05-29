class Node
{
    constructor(value)
    {
        this.value=value
        this.next=null
    }
}

function cycleDetection(head)
{
    let obj={}
    let temp=head 
    while(temp!=null)
    {
        if(temp in obj)
        {
            console.log(obj)
            return temp
        }
        else{
            console.log(obj)
            obj[temp.value]=true
        }
        temp=temp.next
    }
    return null
}

let node=new Node(1)
node.next=new Node(2)
node.next.next=new Node(3)
node.next.next.next=new Node(4)
node.next.next.next.next=new Node(5)
node.next.next.next.next.next=new Node(6)
node.next.next.next.next.next.next=new Node(7)
node.next.next.next.next.next.next.next=new Node(8)
node.next.next.next.next.next.next.next.next=new Node(9)
//node.next.next.next.next.next.next.next.next.next=node.next.next
console.log(cycleDetection(node))
