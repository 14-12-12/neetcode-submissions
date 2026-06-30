
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.size = 1
    def visit(self, url: str) -> None:
        self.cur = self.cur+1
        if (self.cur == len(self.history)):
            self.history.append(url)
            self.size = self.size+1
        else:
            self.history[self.cur] = url
            self.size = self.cur+1
    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
    def forward(self, steps: int) -> str:
        self.cur = min(self.size-1, self.cur+steps)
        return self.history[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)