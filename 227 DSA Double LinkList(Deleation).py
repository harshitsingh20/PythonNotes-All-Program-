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

    def Deleate_begning(self):
        if self.head is None:
            print("LinkList is empty we can't delete the first node")
            return
        if self.head.next is None:
            self.head=None
        else:
            self.head = self.head.next
            self.pre = None

    def Delete_End(self):
        if self.head is None:
            print("LinkList is empty we can't delete the first node")
            return
        if self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.pre.next=None

    def Deleate_by_value(self, x):
        if self.head is None:
            print("LinkList is empty we can't delete the first node")
            return
        if self.head.next is None:
            if x==self.head.data:
                self.head=None
            else:
                print("X is not present in Double LinkList")
            return
        if self.head.data==x:
            self.head=self.head.next
            self.head.pre=None
            return
        temp=self.head
        while temp.next is not None:
            if x==temp.data:
                break
            else:
                temp=temp.next
        if temp.next is not None:
            temp.next.pre=temp.next
            temp.pre.next=temp.next
        else:
            if temp.next==x:
                temp.pre.next=None
            else:
                print("X is not present in Double LinkList")

dll=DoubleLinkList()