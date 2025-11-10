# Time complexity: O(1) for addAtHead. O(k) for get, addAtIndex, and deleteAtIndex, where k is an index of the element to get, add or delete. O(N) for addAtTail.
# Space complexity: O(1) for all operations.
class Node: # we need to implement a node class which are the elements in the linked list
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
            
    def __init__(self): # for the linked list we need the size and head node - we initialize this node to 0
        self.size = 0
        self.head = Node(0)

    def get(self, index: int) -> int:
        if index < 0 or index>=self.size: # index check to make sure index is in bounds, we include the last index
            return -1
        
        cur = self.head # set our pointer to head
        for i in range(index+1): # move the pointer include the index
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: # index bounds check
            return

        if index < 0: # index bounds set 
            index = 0

        cur = self.head # initialize pointer
        for i in range(index): # move the pointer to the node before the index node since we are setting the index to the new node
            cur = cur.next
        
        new = Node(val) # initialize the new node 
        # insert the new node ex [1] -> [3], new node = [2], cur = [1]
        new.next = cur.next # set the new nodes next node [2] -> [3]
        cur.next = new # set the previous nodes [1] -> [2]
        
        self.size+=1  # increment the size of the linked list
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: # index boundary check, include the last index
            return 
        
        cur = self.head # initialize pointer 
        for i in range(index): # move pointer to the node before the indexed node
            cur = cur.next

        cur.next = cur.next.next # remove the node 
        # example [1]->[2]->[3]->None remove [3], cur = [2]
        # [1]->[2]->None
        self.size -=1 # decrement the size
    def printList(self): 
        cur = self.head
        for i in range(self.size+1):
            if i == 0:
                print(f"head->", end='')
            elif cur.next != None:
                print(f"{cur.val}->", end='')
            else:
                print(f"{cur.val}->{cur.next}")
            cur = cur.next
obj = MyLinkedList()
param_1 = obj.get(0)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.addAtTail(4)
obj.addAtTail(5)
obj.addAtTail(6)
obj.printList()
param2 = obj.get(2)
print(param2)
obj.deleteAtIndex(2)
obj.printList()
param2 = obj.get(3)
print(param2)