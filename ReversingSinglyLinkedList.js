class Node
{
    constructor(value)
    {
        this.value=value 
        this.next=null

    }
}

function reversing(head)
{
    let prev=null;
    let cur=head;
   
    while( cur)
    {
        let next1=cur.next;
        cur.next=prev 
        prev=cur 
        cur=next1 
        
    }
    return prev 
}
function printing(head1)
{
    let temp=head1 
    while(temp!=null)
    {
        console.log(temp.value)
        temp=temp.next
    }
}

let node=new Node(1)
node.next=new Node(2)
node.next.next=new Node(3)
node.next.next.next=new Node(4)
let root=reversing(node)
printing(root)