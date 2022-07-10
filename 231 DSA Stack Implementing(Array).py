class Stack(object):
    def __init__(self):
        self.items=[]

    def push(self,value):
        self.items.append(value)

    def pop(self):
        self.items.pop()
        pass
    def peek(self,value):                   #This will Give the last element of stack
        if self.items is not None:
            return self.items[-1]
        else:
            return None


    def size(self):
        if self.items is not None:
            return len(self.items)
        else:
            return None

    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False

    def top(self):
        if self.items is None:
            return "Empty Stack"

        if self.items is not None:
            return self.items.index(3)



if __name__ == '__main__':
    stack = Stack()       #Object
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.items)
    # print(stack.size())
    print(stack.peek(0))
    print(stack.top())

    # stack.pop()
    # print(stack.size())
    # print(stack.isEmpty())