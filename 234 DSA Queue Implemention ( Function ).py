queue = []

def enqueue():
    if len(queue) == n:
        print("Queue is Full")
    else:
        element = int(input("Enter the the Element: "))
        queue.append(element)
        print(element ," Is added to the queue")
def dequeue():
    if not queue:
        print("Queue is Empty")
    else:
        e = queue.pop(0)
        print(e , "This element is removed")
def printDetails():
    print(queue)
n = int(input("Select the Length of the Queue: "))
while True:
    print("1) for enqueue  2) for dequeue  3) for Print Queue  4) Quit")
    choice = int(input("Enter the Choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        printDetails()
    elif choice == 4:
        break
    else:
        print("Please input Valid Input")