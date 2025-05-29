// Problem Remove all the node in the linked list which is matching withe given value

class Node 
{
    constructor(value)
    {
        this.value=value;
        this.next=null;
        this.prev=null;

    }
}

class DoublyLinkedList
{
    constructor()
    {
        this.head=null;
        this.tail=null;

    }
    print()
    {
        let temp=this.head;
        while(temp)
        {
            console.log(temp.value)
            temp=temp.next;
        }
    }
    addAtTail(value)
    {
        let node=new Node(value)
        if(this.head==null)
        {
            this.head=node;
            this.tail=node;
        }
        else
        {
            node.prev=this.tail
            this.tail.next=node
            this.tail=node  

        }
        return this.head;
    }
    remove(node)
    {
        //node to be removed is at head
        if(this.head==node) this.head=node.next;
        //node to be removed is at tail
        if(this.tail==node) 
        {
            this.tail=node.prev ;
           
        }
        // if not node is at intermediatory position
        if(node.prev) 
        {
            //if 2 to be removed i.e, node is 2
            //1->2->3->4->null
            node.prev.next=node.next 
        }
        if(node.next)
        {
            node.next.prev=node.prev
        }

        node.prev=null;
        node.next=null;

    }

    removeAllNodes(value)
    {
        let temp=this.head;
        while(temp)
        {
            let cur=temp;
            temp=temp.next;
            if(cur.value==value)
            {
                this.remove(cur)
            }
        }
    }
}

const double=new DoublyLinkedList()
// double.addAtTail(20)
// double.addAtTail(20)
// double.addAtTail(20)
// double.addAtTail(10)
// double.addAtTail(20)
// double.addAtTail(20)
// double.addAtTail(20)
double.print()
double.removeAllNodes(20)
console.log()
double.print()


