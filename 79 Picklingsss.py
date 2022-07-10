# Pickling is a process of serializing an object. Serializing means to store the object in the form of binary
# representation so it can be saved in our main memory. The object could be of any type. It could be a string, tuple,
# or any other sort of object that Python supports.



# In this example, we will pickle a dictionary. We will save it to a file and then load again.


import pickle

# Pickling a python object

# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "80 mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()


# unpickling

file = "80 mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = ?




