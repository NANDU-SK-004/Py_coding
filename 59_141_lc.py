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
g= Node(7)



a.next=b
b.next=c
c.next=d
d.next=e
f.next
f.next=g
g.next=c

class Singly:
    def __init__(self, head):
        self.head = head
    def traverse(self):
        curr =self.head
        while curr is not None:
            print(curr.val)
            curr =curr.next
   
a =Singly(a)
a.traverse()

