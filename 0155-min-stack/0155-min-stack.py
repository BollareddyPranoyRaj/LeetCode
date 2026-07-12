class MinStack:

    def __init__(self):
        self.s=[]
        self.mini=[]
        

    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.mini:
            self.mini.append(value)
        else:
            self.mini.append(min(value, self.mini[-1]))
        

    def pop(self) -> None:
        if self.s and self.mini:
            self.s.pop()
            self.mini.pop()

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()