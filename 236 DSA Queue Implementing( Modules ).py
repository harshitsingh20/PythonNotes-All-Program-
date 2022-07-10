import queue # Priority Queue: - It takes Lowest Number as the highest Priority (Sort). It remove lowest first

q = queue.PriorityQueue()  #PriorityQueue is also known as Binary heap

q.put(10)
q.put(50)
q.put(20)
q.put(40)
q.put(90)
q.put(80)

a = q.get()
print(a)


# Tuple:- Insert PriorityQueue in Tuple and Value

#
# q = []
# q.append((1,"Harshit"))
# q.append((2,"Ankit"))
# q.append((9,"Renu"))
# q.append((0,"Anjani"))
# q.append((5,"Khushi"))
#
# q.sort(reverse=True)      # Sort and reverse the value
#
# print(q)