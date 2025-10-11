class MyQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        
    def push(self, x: int) -> None:
        if not self._stack1:
            self._stack1.append(x)
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            self._stack1.append(x)
            while self._stack2:
                self._stack1.append(self._stack2.pop())

    def pop(self) -> int:
        return self._stack1.pop()

    def peek(self) -> int:
        return self._stack1[-1]

    def empty(self) -> bool:
        return len(self._stack1) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()