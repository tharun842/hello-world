class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
   
    def AddNode(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
       
    def deleteNode(self):  
        #store head node
        temp=self.head
       
        #if head node is empty
        if(temp != None):
            self.head=temp.next
           
    def search(self,key):
        temp=self.head
        while temp != None:
            if temp.data==key:
                return True
            else:
                temp=temp.next
        return False
    def display(self):
        temp=self.head
        while temp != None:
            print(temp.data,end='->')
            temp=temp.next
        print('Null')
       
#main
L1=Linkedlist()
L1.AddNode(5)
L1.AddNode(15)
L1.AddNode(35)
L1.AddNode(45)
print("linked list after adding:")
L1.display()
L1.deleteNode()
print("linked list after deleting:")
L1.display()
res=L1.search(10)
if res==True:
    print("searching:element present")
else:
    print("searchig:element not present")
   
#graph
import matplotlib.pyplot as p
p.title("singly linked list-graph for asymptotic notation")
p.xlabel("input size")
p.ylabel("steps")
x=list(range(1,100))
y1=[1 for y in x]
y2=[y for y in x]
p.plot(x,y1,'r',label='o((1))-inserting/deleting a node')
p.plot(x,y2,'y',label='o(n)-search/display nodes')
p.legend()
p.show()  