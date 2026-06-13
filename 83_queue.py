class Queue :
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items) ==0
    
    def enqueue(self ,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("empty list")
            return
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items)==0 :
            print("empty")
            return
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            print("empty")
        return self.items[-1]

    def prr(self):
        return self.items
   
a = Queue()
a.enqueue(56)
print(a.prr())