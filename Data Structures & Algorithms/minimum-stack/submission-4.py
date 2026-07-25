class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_min_stack = []
        self.max = 2 ^ 31 - 1
        self.min = self.max

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min = val
        else:
            if val < self.min:
                self.min = val
        self.stack.append(val)
        self.prefix_min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_min_stack.pop()
        self.min = self.getMin()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.prefix_min_stack) == 0:
            return self.max
        return self.prefix_min_stack[-1]
        
