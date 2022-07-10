#Instance variable:- are the variables for which the value of the variable is different
# for every instance.

#Class variable:- Class attributes are owned by the class directly, which means that they are
# not tied to any object or instance.

# The __dict__ attribute:- object.__dict__                 Return Dictionary

class Employee:
    no_of_leaves = 8        #Methods
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)        #return in dictionary type
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)
