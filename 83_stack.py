class Stack :
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items) ==0
    
    def push(self ,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("empty list")
            return
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            print("empty")
        return self.items[-1]
    
    def prr(self):
        return self.items

a = Stack()
a.push(56)
a.push(34)
print(a.top())
print(a.prr())