class ListNode:
    
    def __init__(self, x: int):
        self.val = x
        self.prev = None
        self.next = None
        

class MyLinkedList:

    def __init__(self): # when we initialize we need sentinels or reference nodes for the heads and tails 
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail # assign head.next to tail
        self.tail.prev = self.head # assign tail.prev to head 

    def get(self, index: int) -> int: # Time O(N) - access is always O(N)
        if index < 0 or index >= self.size:
            return -1
        
        if index+1 < self.size - index: # we can cut access time depending on the index we want to access:   starting from the head: index+1 is distance from head to index, self.size-index = distance from tail to index
            cur = self.head
            for _ in range(index+1):
                cur = cur.next
        else:
            cur = self.tail
            i = 0
            for _ in range(self.size - index):
                cur = cur.prev
        return cur.val

    def addAtHead(self, val: int) -> None: #Time O(1) - add node between the old head and head sentinel
        newNode = ListNode(val)
        cur,succ = self.head, self.head.next
        cur.next = newNode
        newNode.prev = cur
        newNode.next = succ
        succ.prev = newNode
        self.size+=1

    def addAtTail(self, val: int) -> None: # Time O(1) add node between the old tail and tail sentinel 
        newNode = ListNode(val)
        cur,pred = self.tail, self.tail.prev
        newNode.prev = pred
        newNode.next = cur
        pred.next = newNode
        cur.prev = newNode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None: #Time O(1)
        if index > self.size: # if the index does not exist we return 
            return
        if index < 0: # if the index is negative add the new node to the head
            index = 0
            
        newNode = ListNode(val)
        
        # in this condition we want to land on the predecessor node - node before the index
        if index < self.size-index: # again depending on the index we want to insert at we dete
            pred = self.head
            for _ in range(index): 
                pred = pred.next
            succ = pred.next
        else: # in this condition we want to land on the successor node - node at the index which will becomre the sucessor node to the new node
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
                
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode
        
        self.size+=1 
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: # return if index is not in bounds 
            return
        
        # in this condition  we want to land on the predecessor node - node before target 
        if index < self.size-index: # distance from first real node to index vs distance from last real node to index 
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else: # want to land on successor node node after target
            succ = self.tail
            for _ in range(self.size-index-1): # we stop 1 node past the target to access neighbors # head 0   1   2   3   4   5  tailindex = 4 6-4-1 = 1 
                succ = succ.prev # at 5 
            pred = succ.prev.prev # want 3 
        pred.next = succ # 3 <-> 5 
        succ.prev = pred
        self.size-=1