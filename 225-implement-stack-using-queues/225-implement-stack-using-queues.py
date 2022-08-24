class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.insert(0,x)

    def pop(self) -> int:
        self.q2 = self.q1[::-1]
        res = self.q2.pop()
        self.q1 = self.q2[::-1]
        self.q2.clear()
        return res

    def top(self) -> int:
        self.q2 = self.q1[::-1]
        re = self.q2[-1]
        self.q2.clear()
        return re
        

    def empty(self) -> bool:
        return len(self.q1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()