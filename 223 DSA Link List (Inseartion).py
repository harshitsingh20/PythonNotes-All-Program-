class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def printList(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,"-->",end=" ")
                temp = temp.next

    def add_at_begnin(self,data):
        new_node = Node(data)       #Object
        new_node.next = self.head
        self.head = new_node

    def add_the_end(self,data):
        new_node = Node(data)       #Object
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in LinkList")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == x:         #Before First Node
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # Totoyas Method
    def printMiddle(self):
        slow = self.head
        fast = self.head  # These two are base condition
        while fast and fast.next:  # fast :- Croces the Boundation(last point)
            slow = slow.next  # fast.next:- Reaches the last Value
            fast = fast.next.next
            print("The middle element is ", slow.data)

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
        else:
            self.head = self.head.next



li = LinkList()             #Object


# li.add_at_begnin(20)
# li.add_the_end(100)             #Isko Dheak Lo
# li.add_after(200,100)
# li.add_at_begnin(10)
li.add_at_begnin(20)
# li.delete_begin()

print(li.printList())