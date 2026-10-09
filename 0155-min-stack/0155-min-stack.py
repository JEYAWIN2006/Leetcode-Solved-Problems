class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, val: int) -> None:
        if self.stack:
            self.min_num = min(self.min_num, val)
        else:
            self.min_num = val
        self.stack.append([val, self.min_num])

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_num = self.stack[-1][1]
        else:
            self.min_num = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_num