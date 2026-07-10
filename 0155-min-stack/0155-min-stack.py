class MinStack:

    def __init__(self):
        self.st = []
        self.mini = []

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mini or value <= self.mini[-1]:
            self.mini.append(value)

    def pop(self) -> None:
        if self.st:
            if self.st.pop() == self.mini[-1]:
                self.mini.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if self.mini:
            return self.mini[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()