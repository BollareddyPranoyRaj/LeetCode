class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        if self.s1 or self.s2:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()