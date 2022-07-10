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

    def min_node(self):
        current = self
        while current.left:
            current = current.left
        print("Smallest key is is ", current.key)

    def max_node(self):
        current = self
        while current.right:
            current = current.right
        print("Maximum key is ", current.key)