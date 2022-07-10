# enumerate gives index and item both
l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]
"""
i = 1
for item in l1:
    if item%2 is not 0:
        print(f"Jarvis please buy {item}")
        i += 1
"""
# for index, item in enumerate(l1):
#     if index%2==0:
#         print(f"Jarvis please buy {item}")

color = ["red", "yellow", "Green"]
for i ,j in enumerate(color):
    print(i,j)