class MinStack:
    def __init__(self):
        self.item = []
        
    def push(self, x: int):
        self.item.append(x)
        
    def pop(self):
        return self.item.pop()
        
    def top(self):
        return self.item[-1]
        
    def getMin(self):
        return min(self.item)
