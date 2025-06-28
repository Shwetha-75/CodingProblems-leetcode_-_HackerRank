class Node{
    constructor(value)
    {
        this.value=value;
        this.next=null;
        this.prev=null;
    }
}

class LinkedList
{
    constructor()
    {
        this.head=null;
        this.tail=null;
    }

    addATTail(value)
    {
        let node=new Node(value);
        if(this.head===null)
        {
            this.head=node;
            this.tail=node;
        }
        else
        {
            this.tail.next=node;
            node.prev=this.tail;
            this.tail=node;

        }
    
    }


    remove(node)
    {
        if(this.head===node) 
        {
            let temp=this.head;
            this.head=temp.next;
            temp.next=null;
            this.head.prev=null;
        }
        else if(this.tail===node)
        {
            let temp=this.tail;
            this.tail=temp.prev;
            temp.prev=null;
            this.tail=null;
        }
        else{
            let temp1=node.prev;
            let temp2=node.next;
            node.prev=null;
            node.prev=null;
            temp1.next=temp2;
            temp2.prev=temp1;
        }
    }

        insertPosition(nodePosition,nodeInsert)
        {
            //observations
            //1 check whether we have only one node in the double lik=nked list 
            //and that itself is a nodeInsert means we have to return as it is
            if(this.head===nodeInsert && this.tail===nodeInsert)
            {
                return;
            }
            //observations
            //nodeInsert is a part of linked list 
            this.remove(nodeInsert);
            //advance the field(next)  of nodeInsert 
            nodeInsert.next=nodePosition;
            //check whether the nodePosition is a head 
            if(nodePosition===this.head)
            {
                this.head=nodeInsert;
            }
            else
            {//   <-- <-- <-- <-- <--  <--
                //1-->2-->3-->4-->5-->6-->null
                //    |
                //  nodePosition-->1 should point to the nodeInsert
                nodePosition.prev.next=nodeInsert
            }

            //coomon for all insertion
            nodePosition.prev=nodeInsert;
           return this.head;
        }
    }