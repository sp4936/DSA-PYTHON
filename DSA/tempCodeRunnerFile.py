class Stack:
    def __init__(self):
        self.lst = []
        
    def is_empty(self):
        return len(self.lst) == 0
    
    def push(self,data):
        self.lst.append(data)
    
    def pop(self):
        self.lst.pop()
        
    def peek(self):
        return self.lst[-1]
        
    def size(self):
        return len(self.lst)
    
s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.peek()
s1.pop()
s1.peek()