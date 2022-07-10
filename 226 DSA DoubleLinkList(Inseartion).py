class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

class DoubleLinkList:
    def __init__(self):
        self.head = None

    def printList_Forward_direction(self):              #Traversal Example
        if self.head is None:
            print("LinkedList is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,"-->",end=" ")
                temp = temp.next

    def printList_backward_direction(self):         #Reverse
        if self.head is None:
            print("LinkList is Empty")
        else:
            temp=self.head
            while temp.next is not  None:           #We Reach to the Last Node
                temp=temp.next
            while temp is not None:
                print(temp.data,"-->",end=" ")
                temp=temp.pre

    def insert_LinkList_Empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("LinkList is Not Empty!")

    def insert_Begning(self,data):
        new_Node=Node(data)
        if self.head is None:
            new_Node=self.head
        else:
            new_Node.next=self.head
            self.head.pre=new_Node
            self.head=new_Node

    def insert_End(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.pre = temp

    def add_after(self,data,x):
        if self.head is None:
            print("Empty LinkList")
        else:
            temp=self.head
            while temp is not None:
                if x==temp.data:
                    break
                else:
                    temp=temp.next
            if temp.next is None:
                print("LinkList is not found!!")
            else:
                new_node=Node(data)
                new_node.next=temp.next
                new_node.pre=temp
                if temp.next is not None:
                    temp.next.pre=new_node
                temp.next=new_node

    def add_Before(self,data,x):
        if self.head is None:
            print("Empty LinkList")
        else:
            temp=self.head
            while temp is not None:
                if x==temp.data:
                    break
                else:
                    temp=temp.next
            if temp.next is None:
                print("LinkList is not found!!")
            else:
                new_node=Node(data)
                new_node.next=temp
                new_node.pre=temp.pre
                if temp.pre is not None:
                    temp.pre.next=new_node
                temp.pre=new_node


dll=DoubleLinkList()

dll.insert_End(30)
dll.insert_LinkList_Empty(10)
dll.insert_Begning(20)
print(dll.printList_Forward_direction())