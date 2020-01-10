class MyQueue:
    def __init__(self):
        self.item = []
        
    def push(self, x: int):
        return self.item.append(x)
        
    def pop(self):
        return self.item.pop(0)
        
    def peek(self):
        return self.item[0]
        
    def empty(self):
        if len(self.item)==0:
            return True
        else:return False
