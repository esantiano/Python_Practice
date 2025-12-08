# Time: O(1) - amortized analysis for each operation. O(n) worst case for push
# Space  O(n) - we use n space for the stacks 
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # we'll use s1 as the actual queue
        # if theres nothing in s1 then we can append to s1
        # otherwise we push the top of s1 into s2 until s1 is empty, then push x onto s1 and put everything in s2 back into s1
        if not self.s1:
            self.s1.append(x)
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s1.append(x)
            while self.s2:
                self.s1.append(self.s2.pop())

    def pop(self) -> int:
        # here we can just pop from s1
        return self.s1.pop()
    def peek(self) -> int:
        # here we return the top value from s1
        return self.s1[-1]
    def empty(self) -> bool:
        # here we return whether or not s1 is empty
        return False if self.s1 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()