for rows in range(7):
    for column in range(5):
        if ((column == 0 or column == 4) and rows!=0) or (rows==0 or rows==3) and (column>0 and column<4):
            print("*",end="")
        else:
            print(end=" ")
    print()