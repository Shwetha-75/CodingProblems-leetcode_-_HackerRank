class Node{
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
            let temp=this.tail;
            this.tail.next=node;
            node.prev=temp 
            this.tail=node;

        }
        return this.head
    }
    printing()
    {
        let temp=this.head
        while(temp)
        {
            console.log(temp.value)
            temp=temp.next
        }
   
    }
}

const double=new DoublyLinkedList()

double.addAtTail(1)
double.addAtTail(2)
double.addAtTail(3)
double.addAtTail(4)
double.addAtTail(5)
double.printing()


