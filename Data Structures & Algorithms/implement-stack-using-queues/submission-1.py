class MyStack:

    def __init__(self):
        self.queue1 = []
    def push(self, x: int) -> None:
        self.queue1.append(x)
    def pop(self) -> int:
        if (len(self.queue1)==0):
            return -1
        else:
            number = self.queue1.pop(-1)
        return number

    def top(self) -> int:
        if (len(self.queue1)==0):
            return -1
        else:
            number = self.queue1[-1]
        return number
    def empty(self) -> bool:
        if (len(self.queue1)==0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()