class Node :
    def __init__(self ,val):
        self.val =val
        self.next =None

class Singly_Linked_List:
    def __init__(self):
        self.head =None
    def append(self ,val):
        new_node =Node(val)
        if self.head == None :
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not  None:
                curr = curr.next
            curr.next =new_node
    
    def traverse(self):
        curr = self.head
        if self.head is None:
            print("empty")
        else:
            while curr is not  None:
                print(curr.val)
                curr = curr.next
    
    def insert_midway(self ,val ,position):
        new_node =Node(val)
        if position == 0:
            new_node.next =self.head
            self.head =new_node
        else:
            curr = self.head
            previous_node = None
            count =0
            while count != position and curr is not None:
                count +=1
                previous_node =curr
                curr =curr.next
            previous_node.next =new_node
            new_node.next =curr

    def first_ele(self ):
        if self.head == None :
            print("valla panikkum poda")
        
        elif self.head.next ==None :
            self.head = None
            print("no elelment here")
        
        else:
            temp  =self.head
            self.head =self.head.next
            temp .next =None

    def delete(self ,val):
        temp =self.head
        if temp.next is not None:
            if temp.val ==val:
                self.head =temp.next
                return
            else:
                found =False
                prev =None
                while temp is not None:
                    if temp.val == val:
                        found =True
                        break
                    prev =temp
                    temp =temp.next
                if found :
                    prev.next =temp.next
                    return
                else:
                    print("None not found")



    


a =Singly_Linked_List()
a.append(3)
# a.append(8)
# a.traverse()
# a.insert_midway(4 ,1)
# a.traverse()
a.traverse()
a.first_ele()