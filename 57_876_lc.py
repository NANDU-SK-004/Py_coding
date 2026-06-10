class Node:
    def __init__(self ,val):
        self.next =None
        self.val =val

a= Node(1)
b= Node(2)
c= Node(3)
d= Node(4)
e= Node(5)
f= Node(6)
c.next=d
g= Node(7)
d.next=e
h= Node(8)

a.next=b
b.next=c
g.next=h
f.next=g
e.next=f

class Singly:
    def __init__(self, head):
        self.head = head
    def traverse(self):
        curr =self.head
        while curr is not None:
            print(curr.val)
            curr =curr.next
    def traverse2(self):
        prev =self.head
        curr =self.head
        while curr is not None and curr.next is not None :
            prev =prev.next
            curr =curr.next.next
            
        print(prev.val)
a =Singly(a)
a.traverse2()

