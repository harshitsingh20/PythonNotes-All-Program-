# 1) By Using Collections Module


# import collections
# queque = collections.deque()
# queque.appendleft(10)             #Append to left side
# queque.appendleft(20)
# queque.appendleft(30)
# queque.appendleft(40)
# queque.appendleft(50)




# queque = collections.deque()
# queque.append(10)
# queque.append(20)
# queque.append(30)
# queque.append(40)
# queque.append(50)
#
# queque.popleft()                    #pop to the left side
#
# print(queque)



# 2) By using Queue Module


import queue

q = queue.Queue()

q.put(10)                   # Add Element in Queue(put)
q.put(20)
q.put(30)
q.put(40)
q.put(50)

q.get()                      # Remove Element in Queue(get)

print(q)