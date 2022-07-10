# class Node:
#     def __init__(self, item):
#         self.left = None
#         self.right = None
#         self.val = item
#
#
# def inorder(root):
#
#     if root:
#         # Traverse left
#         inorder(root.left)
#         # Traverse root
#         print(str(root.val) , "->", end=' ')
#         # Traverse right
#         inorder(root.right)
#
#
# def postorder(root):
#
#     if root:
#         # Traverse left
#         postorder(root.left)
#         # Traverse right
#         postorder(root.right)
#         # Traverse root
#         print(str(root.val) , "->", end=' ')
#
#
# def preorder(root):
#
#     if root:
#         # Traverse root
#         print(str(root.val) , "->", end=' ')
#         # Traverse left
#         preorder(root.left)
#         # Traverse right
#         preorder(root.right)
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print("Inorder traversal ")
# inorder(root)
#
# print("\nPreorder traversal ")
# preorder(root)
#
# print("\nPostorder traversal ")
# postorder(root)


# User Input in Binary Serrch Tree

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


    def preOrder(self):
        print(self.key, '-->', end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.key, '-->', end=" ")

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.key,'-->',end=" ")
        if self.right:
            self.right.inOrder()


root = Binary_search_tree(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
root.preOrder()