class Binary_search_tree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.left:                   #self.left is not None
                self.left.insert(data)
            else:
                self.left = Binary_search_tree(data)            #Creating New Node of left child
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Binary_search_tree(data)

    def deletes(self, data):
        if self.key is None:
            print("Tree is Empty!!")
            return
        if data < self.key:
            if self.left:
                self.left = self.left.deletes(data)
            else:
                print("Data is not present in tree")
        elif data > self.key:
            if self.right:
                self.right = self.right.deletes(data)
            else:
                print("Data is not present in tree")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.deletes(node.key)
        return self
root = Binary_search_tree(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
root.deletes(6)