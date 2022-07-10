# 1) Collection Modules: deque(Double Ended Queue)

# import collections
# stack=collections.deque()       #Creation of stack in modules
# print(stack)        #Empty Stack
#
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
#
# print(stack)
#
# stack.pop()
# stack.pop()
#
# print(stack)


# 2) Queue :- LifoQueue

import queue

stack = queue.LifoQueue()       #Creation of Stack    # In this We can put the Limit also
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40, timeout=1)

print(stack)