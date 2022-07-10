#Their are two types od traversal
#1) Forward Traversal
#2 Backward Traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None

class DoubleLinkList:
    def __init__(self):
        self.head=None

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
            while temp.next is not None:           #We Reach to the Last Node
                temp=temp.next
            while temp is not None:
                print(temp.data,"-->",end=" ")
                temp=temp.pre
dll=DoubleLinkList()

print(dll.printList_backward_direction())