class Node(object):
    def __init__(self,data=None, next=None):
        self.data = data
        self.next=next
class Circular_Linklist(object):
    def __init__(self,head=None, end=None):
        self.head=head
        self.tail=end

    def traversa(self):
        temp = self.head
        while temp.next:
            print(temp.data,"-->",end=" ")
            temp = temp.next
            if temp == self.head:
                break

    def insert_END(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.next = new_node
            self.end = new_node
            return
        if self.end != None:
            self.end.next = new_node
            new_node.next = self.head
            self.end = new_node
            return

    def insert_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        temp = self.head
        if temp == None:
            self.head = new_node
            self.end = new_node
            self.head.next = new_node
            return
        if self.end != None:
            self.end.next = new_node
            new_node.next = self.head
            self.head = new_node
            return