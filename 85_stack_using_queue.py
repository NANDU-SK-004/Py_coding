from collections import deque
class StackUsingQueue :
    def __init__(self):
        self.queue=deque()

    def push(self ,val):
        self.queue.append(val)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "empty"
        return self.queue.popleft()
    
    def top(self):
        if len(self.queue) == 0:
            return "empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def prr(self):
        return self.queue
c =StackUsingQueue()
c.push(2)
c.push(7)
c.push(8)    
print(c.prr())
c.pop()
print(c.prr())