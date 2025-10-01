class Stack:
    def __init__(self, *args):
        self.stack = list(args)
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return self.stack
    
    def peek(self):
        return self.stack[0]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else: False
        
    def size(self):
        return len(self.stack)

s = Stack(1, 2, 3, 4, 5)
print("Size after push:", s.peek())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())