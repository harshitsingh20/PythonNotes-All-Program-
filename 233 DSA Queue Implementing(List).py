# First Method

# queue = []      #Empty Queue
# queue.append(10)            # append means: -  enqueue (Insert)
# queue.append(20)
# queue.append(30)
# queue.append(40)
#
# queue.pop(0)                # pop means : - dequeue (Remove)
#
# print(queue)



# Second Method


# queue = []
# queue.insert(0,10)                  # append means: -  enqueue (Insert)
# queue.insert(0,20)
# queue.insert(0,30)
# queue.insert(0,40)
# queue.insert(0,50)
#
#
# queue.pop()                         # pop means : - dequeue (Remove)
#
# print(queue)


# Check Weather the queue is Empty or not
# It Returns True and False value
# queue = []
# a = not queue
# print(a)



queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print(queue[-1])            # This gives the last element of the Queue

print(queue[0])             # This gives the First element of the Queue



# Implementing Queue in List

# class Queue:
#     def __init__(self):
#         self.item=[]
#     def add(self,value):
#         self.item.append(value)
#     def rem(self,index):
#         if self.item is None:
#             print("Queue is Empty")
#         else:
#             self.item.pop(0)
#             pass
#     def peek(self):
#         if self.item is None:
#             print("Queue is Empty")
#         else:
#             return self.item[-1]
#     def size(self):
#         if self.item is None:
#             print("Queue is Empty")
#         else:
#             return len(self.item)
#
# qu = Queue()
#
# qu.add(10)
# qu.add(20)
# qu.add(30)
# qu.add(40)
# qu.add(50)
#
# qu.rem(0)
#
# print(qu.item)
