class Employee:
    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return 99
Harshit = Employee()
Harshit.name = "Harshit"
print(Harshit.printgood('Ankit'))