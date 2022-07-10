"""
1) print(dir(os)):- It gives us a list of all the functions the OS module is composed of.

2) os.getcwd( ):- Here cwd is a short form for the current working directory. The function
returns us the path of the directory we are currently in. It is important to know about our
directory because when we are trying to import a file in python, the compiler searches for
it in our current directory.

3) os.chdir( ):- it is used in case we want to change our directory. The new path is sent
inside the parenthesis. If we want to access some files or folder from some other directory,
we can use it.

4) os.listdir( ):-If we want to output the names of all the directories at a certain location,
we can use this function.

5) os.mkdir( ):- To create a new directory or folder. The name is sent as a parameter inside the
parenthesis.

6) os.makedirs( ):- To make more than on directory simultaneously.

7) os.rename( ):- To rename an already existing directory, we use this. We send the current name
and new name of our directory as parameters

8) os.rmdir( ):- It deletes an empty directory.

9) os.removedirs( ):- We can remove all directories within a directory by using removedirs().

10)
"""





import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
