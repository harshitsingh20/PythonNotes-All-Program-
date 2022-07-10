# Make a List and we have to detect weather it is a number or not if that was a number so check weather the
# number is greater than 6 or not

list1 =[5,7,2,"Harshit","Sherya","Simran",3,9]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item,end=" ")