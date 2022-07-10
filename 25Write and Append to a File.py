# f = open("26harshit.txt", "w")
# a = f.write("Harshit bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("26harshit.txt", "a")
# a = f.write("Harshit bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("26harshit.txt", "r+")
g=f.read()
print(g)
f.write("\nthank you")
f.close()