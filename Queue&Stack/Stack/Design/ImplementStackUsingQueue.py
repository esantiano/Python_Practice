# Time: O(1) for most operations except push and top which are O(n)
# Space: O(n) we ust this space for both queues 

# Design we use two queues in this design the primary stack being q1
# For push we empty q1 into q2, add x into q1 and then add everything from q2 back into q1
# For top we remove the first element in q1 and then add it back to the stack is unchanged
import queue
class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x: int) -> None:
        while self.q1.qsize()>0:
            self.q2.put(self.q1.get())
        self.q1.put(x)
        while self.q2.qsize()>0:
            self.q1.put(self.q2.get())

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        x = self.q1.get()
        self.push(x)
        return x

    def empty(self) -> bool:
        return self.q1.qsize()==0

# this question can be solved by using a single queue 
class MyStack2:

    def __init__(self):
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)
        size = self.q.qsize()
        while size > 1:
            self.q1.put(self.q1.get())
            size -=1
            
    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        x = self.q1.get()
        self.push(x)
        return x

    def empty(self) -> bool:
        return self.q1.qsize()==0