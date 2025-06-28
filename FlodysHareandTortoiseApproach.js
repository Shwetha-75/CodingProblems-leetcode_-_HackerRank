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
    //Observations
    if(!head) return null;
    if (!head.next) return null;
    let tortoise=head
    let hare=head 
    //until hare !=null and hare.next!=null 
    //mistake in the first approach was we have taken into consideration that
    //while loop should run until tortoise and hare bot should not be equal
    while(hare && hare.next)
    {
        tortoise=tortoise.next 
        hare=hare.next.next 
        if(hare!=tortoise)//here if they both met and we can break the loop
        {
            break;
        }
    }
    //observation for linked list not having the cycle 
    if(hare!=tortoise)
    {
        return null;
    }
    let ptr=head 
    //if the tortoise and ptr are equal means we have the cycle in the linked list
    //run until ptr and tortoise met 
    while(ptr!=tortoise)
    {
        ptr=ptr.next;
        tortoise=tortoise.next;
    }
    return ptr
}

node=new Node(1)//                           1-->2-->3-->4-->5-->6-->7-->8-->9
node.next=new Node(2)//#                             |                       |
node.next.next=new Node(3)//#                        -------------------------                   
node.next.next.next=new Node(4)//
node.next.next.next.next=new Node(5)//
node.next.next.next.next.next=new Node(6)//
node.next.next.next.next.next.next=new Node(7)//
node.next.next.next.next.next.next.next=new Node(8)//
node.next.next.next.next.next.next.next.next=new Node(9)//
node.next.next.next.next.next.next.next.next.next=node.next.next