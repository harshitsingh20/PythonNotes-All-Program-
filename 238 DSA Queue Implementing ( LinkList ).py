class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.Front = None
        self.rear = None

    def enqueue(self,data):
        new_Node=Node(data)
        if self.rear is None:
            new_Node = self.rear
        else:
            while self.rear is not None:
                self.rear = self.rear.next
            self.rear.next = new_Node
            new_Node = self.rear

    def dequeue(self):
        if self.Front is None:
            print("Queue is Empty")
        else:
            temp = self.Front.data
            self.Front = self.Front.next
            return temp

    def is_Empty(self):
        return self.Front is None

    def isPeek(self):
        return self.rear[-1]