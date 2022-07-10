"""
Uses of time modules:
We can use the time module

In games where missions depend on a certain time limit.
To check the execution time a certain part of our code is taking.
To print the date or local time onto the screen
To suspend the execution of python thread.
To measure the efficiency of the code.

"""

import time
initial = time.time()        # It's counts numbers of Ticks

k = 0
while(k<45):
    print("This is harry bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 =time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)