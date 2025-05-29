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
    
    let prev=null
    current=head 
    while(current)
    {
        let next =current.next
        current.next=prev
        prev=current
        current=next
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

let node=new Node(10)
node.next=new Node(20)
node.next.next=new Node(30)
node.next.next.next=new Node(40)
let root=reversing(node)
printing(root)