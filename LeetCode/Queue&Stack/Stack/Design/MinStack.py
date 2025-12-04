# Time: O(1) each operation only takes O(1) time 
# Space: O(n) we use space for every push call
# Design: to ensure we can keep track of the minimum value we store each value as a tuple with the given and minimum
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            cur_min = self.stack[-1][1]
            cur_min = min(cur_min,val)
            self.stack.append((val,cur_min))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Design: use two stacks, one to keep track of the current stack and another to keep track of the minimum values
class MinStack2():
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)
    
    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
# Design: same approach as above but instead of pushing multiples of the same minimum onto the min stack we can just keep track of the number of repeat mins
class MinStack3():
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val,1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1]+=1
        self.stack.append(val)
    
    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1][0]:
            self.min_stack[-1][1]-=1
        if self.min_stack[-1][1]==0:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1][0]