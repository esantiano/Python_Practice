# Time O(n) - we re-calculate next every time it is called
# Space O(n) - we use a queue to hold all the values initialized by size n
# we need to keep the size of the Moving Average class constant
# we can implement a circular queue class to accomplish this 
# the circular queue class will use enqueue, dequeue, and isFull and isEmpty

class CircularQueue:
    def __init__(self, size: int):
        self.queue = [None]*size
        self.head = 0
        self.capacity = size
        self.count = 0
        
    def enqueue(self,value):
        if self.isFull():
            self.dequeue()
        self.queue[(self.head+self.count)%self.capacity]=value
        self.count+=1
        
    def dequeue(self):
        self.queue[self.head]=None
        self.head=(self.head+1)%self.capacity
        self.count-=1
        
    def isFull(self):
        return self.capacity == self.count
    
class MovingAverage:

    def __init__(self, size: int):
        self.nums = CircularQueue(size)

    def next(self, val: int) -> float:
        self.nums.enqueue(val)
        total = 0
        for num in self.nums.queue:
            if num is not None:
                total += num
        return total/self.nums.count

# This class can be simplified by either incorporating the circular queue class into the moving average class
# or by using the deque library - double sided queue allowing us to maintain a sliding window
# both solutions keep an updated window_sum property for the moving average class which reduces the number of calculations (sliding window) 

# Time O(M) where M is the number of next() calls
# Space O(M) since next() is used to store elements in the queue 

# Incorporated circular queue: the head and tail are always next to eachother 
# Pros: adding a new element it automatically discards the oldest element.
# Unlike deque, we do not need to explicitly remove the oldest element.
# A single index suffices to keep track of both ends of the queue, 
# unlike deque where we have to keep a pointer for each end.


class MovingAverageCircularQueue():
    def __init__(self,size):
        self.size = size
        self.queue = [0]*size
        self.head = 0
        self.window_sum = 0
        self.count = 0
        # tail is calculated using tail=(head+1)modsize
    
    def next(self,val):
        self.count+=1 # update the count first 
        tail=(self.head+1)%self.size
        self.window_sum = self.window_sum-self.queue[self.tail]+val # update the window_sum
        self.head = (self.head+1)%self.size # update the head 
        self.queue[self.head]=val # add the new val to the queue 
        return self.window_sum/min(self.count,self.size) # take the lesser value between the count and the size 

# using deque 
# here we can see the sliding window technique more explicitly 
# the deque can remove from the beginning or end of the queue 

from collections import deque 

class MovingAverageDeque():
    def __init__(self,size):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self,val):
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0 # determine if we need to remove a value from the end of the queue
        self.window_sum = self.window_sum - tail + val
        return self.window_sum/min(self.count,self.size) # take the lesser value between the count and the size 