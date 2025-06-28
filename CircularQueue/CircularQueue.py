'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

'''

class CircularQueue:
    def __init__(self,k:int=0):
        self.circular_queue=[0]*k 
        self.head=0
        self.rear=0
        self.n=k 
        self.count=0
        self.full_status=False  
    def Front(self):
        if self.count==0:
            return -1
        if self.head==0:
            return self.circular_queue[0]
        
        return self.circular_queue[self.head-1]
    def Rear(self):
        if self.count==0:
            return -1 
        if self.rear==0:
           return self.circular_queue[-1]
         
        return self.circular_queue[self.rear-1] 
    def enqueue(self,val:int):
        if self.count==self.n:
            return False
        self.circular_queue[self.rear]=val
        self.count+=1
        self.rear+=1
        if self.rear==self.n:
            self.rear=0
        return True
    def dequeue(self):
        if self.count==0:
            return False
        
        self.head+=1
        if self.head==self.n:
            self.head=0 
        self.count-=1
        return True 
    def isEmpty(self):
        return not self.count 
    def isFull(self):
        return self.count==self.n 

class TestApp:
      def testing_case_one(self):
          test=["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
          values=[[3], [1], [2], [3], [4], [], [], [], [4], []]
          circularQueue=CircularQueue(values[0][0])
          result=[None]
          for i in range(1,len(values)):
              if test[i]=='enQueue':
                 result.append(circularQueue.enqueue(values[i][0]))
              elif test[i]=='deQueue':
                  result.append(circularQueue.dequeue())
              elif test[i]=='isFull':
                  result.append(circularQueue.isFull())
              elif test[i]=='Rear':
                   result.append(circularQueue.Rear())
              print(circularQueue.circular_queue)
          print(result)
          assert result==[None, True, True, True, False, 3, True, True, True, 4]
              
        
            
            
       
        