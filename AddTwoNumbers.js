class Node{
    constructor(value)
    {
        this.value=value;
        this.next=null
    }
}
class LinkedList
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
            this.head=node
            this.tail=node

        }
        else
        {
            this.tail.next=node
            this.tail=node
        }
        return this.head
    }
    print()
    {
        let temp=this.head
        while(temp)
        {
            console.log(temp.value)
            temp=temp.next
        }
    }
}

function addNumber(node1,node2)
{
    let carry=0,sum=0;
    linkedlist=new LinkedList()
    let root=null
    while(node1 || node2 || carry)
    {
        let value1=node1? node1.value:0
        let value2=node2? node2.value:0
        sum=value1+value2+carry
        digit=sum%10
        root=linkedlist.addAtTail(digit)
        carry=Math.floor(sum/10)
         
        node1=node1 ?node1.next :null;
        node2=node2 ? node2.next: null;

    }
    return root

}
const node1=new Node(1)
node1.next=new Node(2)
node1.next.next=new Node(3)

const node2=new Node(1)
node2.next=new Node(2)
node2.next.next=new Node(3)

const root=addNumber(node1,node2)

console.log(root)



