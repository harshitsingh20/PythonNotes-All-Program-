# First Method


class LinkList:                     #Head
    def __init__(self):
        self.head=None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp = temp.next        #Condition


class Node:                         #Nodes
    def __init__(self,data=None):
        self.data = data
        self.next = None


li = LinkList()

firstNode = Node(10)                #Input Data in nodes
secondNode = Node(20)
thirdNode = Node(30)
fourthNode = Node(40)

li.head = firstNode                 #Store Node Address
firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode

print(li.printList())

# Second Method

#
# class Node:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
#
# class LinkList:
#     def __init__(self):
#         self.head=Node()
#
#     def printDetails(self):
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
# FirstNode=Node(10)
# SecondNode=Node(20)
# ThirdNode=Node(30)
#
# li=LinkList
#
# li.head=FirstNode
# FirstNode.next=SecondNode
# SecondNode.next=ThirdNode
#
# print(li.printDetails())