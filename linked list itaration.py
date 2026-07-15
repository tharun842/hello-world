class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        
    def addnode(self,data):
        newnode=node(data)
        newnode.next=self.head
        if self.head!=None:
            self.head.prev=newnode
        self.head=newnode 
    def deletenode(self):
        temp=self.head
        if temp!=None:
            self.head=temp.next
            self.head.prev=None
    def display(self):
        temp=self.head
        print("traversal in forward direction")
        while temp!=None:
            print(temp.data,end="->")
            last=temp
            temp=temp.next
        print("traversal in reverese direction")   
        while last!=None:
            print(last.data,end="->")
            last=last.prev
            
l1=dll()
l1.addnode(10)
l1.addnode(20)
l1.addnode(30)
print("doubly linkedlist after adding node") 
l1.display()
print("doubly linked list after deleting node") 
l1.deletenode()
l1.display()         