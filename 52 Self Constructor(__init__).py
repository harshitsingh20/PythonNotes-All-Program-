#Self
"""
class Employee:
    no_of_leaves = 8

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
harry = Employee()
rohan = Employee()
harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(harry.printdetails())

"""

# __init__ method:- is also called as a constructor in object-oriented terminology.

# Constructor:- Constructor in Python is used to assign values to the variables or data
# members of a class when an object is created.

class Person:
  def __init__(self, aname, aage):
    self.name = aname
    self.age = aage

p1 = Person("John", 36)
print(p1.name)
#Output: John