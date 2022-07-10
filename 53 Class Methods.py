class Student:
    no_of_leaves=10
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
Harshit = Student()
Harshit.name="Harshit"
Harshit.no_of_leaves=50
print(Harshit.no_of_leaves)