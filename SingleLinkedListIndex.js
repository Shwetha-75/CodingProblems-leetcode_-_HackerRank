class Node
{
    constructor(value)
    {
        this.value=value
        this.next=null
        
    }
}

class SingeLinkedList
{
    constructor()
    {
        this.head=null
        this.tail=null
        this.size=0
    }

    get(index)
    {
        //observations
        if(index<0 || index>=this.size)
        {
            return -1
        }
        //returning the index
        const count=0//to keep track of the iteration
        const current=this.head//to hold the head 
        while(count!=index)
        {
            current=current.next
            count++;
        }
        return current;
    }
    addHead(value)
    {
        const node=new Node(value)
        //observations
        if(!this.head)
        {
            this.head=node
            this.tail=node 
        }
        else
        {
            node.next=this.head
            this.head=node

        }
        this.size++;
        return this
    }
    addTail(value)
    {
        const node=new Node(value)
        //observations
        if(!this.head)
        {
            this.head=node
            this.tail=node
        }
        else  
        {                //             tail                tail                    tail
            this.tail.next=node// 1->-2->3->null      1->2->3->4->null      1->2->3->4->null
            this.tail=node

        }
        this.size++;
        return this
    }
    addIndex(index,value)
    {
        
        
        //observations
        if(index<0 || index>this.size)
        {
            return "invaild index"
        }
        if (index===0)
        {
            return this.addHead(value)
        }
        if(index===this.size)
        {
            return this.addTail
        }
        //we have to get the previous index node
        const node=new Node(value)
        let previous=this.get(index-1)
        let temp=previous.next
        previous.next=node;
        node.next=temp;
      
        this.size++;
        return this


    }
    deleteIndex(index)
    {
        if(index<0 || index>this.size)
        {
            return "invalid inde"
        }
        if(index===0)
        {
            const temp=this.head 

            this.head=temp.next
            this.size--;
            return temp.value

        }
        if(index===this.size)
        {
           const previous=this.get(index-1)
            const deletedNode=previous.next
            this.tail=previous
            previous.next=null
            this.size--;
            return deletedNode.value
        }
        //particular index
        const previous=this.get(index-1)
        const deletedNode=previous.next 
        previous.next=deletedNode.next 
        this.size--;
        return deletedNode.value

    }
}

single=new SingeLinkedList()
console.log(single.addHead(10))
console.log(single.addTail(20))
console.log(single.addIndex(1,60))
/*console.log(single.addHead(10))
console.log(single.addHead(10))*/