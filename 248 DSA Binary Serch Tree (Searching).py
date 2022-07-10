# Remove the Duplicate value in Binary search Tree

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


    def Search(self, data):
        if self.key == data:
            print("Node is Found")
            return
        if data < self.key:
            if self.left:
                self.left.Search(data)
            else:
                print("Node is Not present")
        else:
            if self.right:
                self.right.Search(data)
            else:
                print("Node is Not present")
root = Binary_search_tree(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
root.Search(6)