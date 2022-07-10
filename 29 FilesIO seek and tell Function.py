#Tell function :-Is used to tell where is my file pointer is. It gives the index value

f = open("26harshit.txt")
print(f.readline())
print(f.tell())

# Seek function:- Is used to tell from which point i have to start. We have to index value

f = open("26harshit.txt")
f.seek(5) # It will start from index 5
print( f.readline())