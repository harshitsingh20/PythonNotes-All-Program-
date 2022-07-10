
class Cqueue:
    que = []

    def insrt(self,len_of_queue):
        if len(self.que)==len_of_queue:
    #         since a circular queue can have length maximum to the length of queue defined by the user
            print("queue is full.")
        else:
            data = input("Enter the data:")
            self.que.append(data)

    def remo(self):
        if len(self.que) == 0:
            # if length of the queue is 0 the it does not have any data
            print("queue is empty.")
        else:
            pdta = self.que.pop(0)
            print("Data popped is:",pdta)

    def display(self):
        if len(self.que) == 0:
            # if length of the queue is 0 the it does not have any data
            print("queue is empty.")
        else:
            print("Data of the queue are:")
            for i in self.que:
                print(i)

if __name__ == '__main__':
    obj = Cqueue()
    #creating the object
    length_of_queue = int(input("Enter the length of the queue:"))
    # we are using typecasting here to take the input as int
    # if user enters data which can't be typecast into int the it will throw error
    while True:
        choice = input("1 to insert data:\n2 to pop a data:\n"
                       "3 to display the queue:\n4 to exit:")
        if choice == '1':
            obj.insrt(length_of_queue)
        elif choice == '2':
            obj.remo()
        elif choice == '3':
            obj.display()
        elif choice == '4':
            exit()
        else:
            print("wrong choice try again")