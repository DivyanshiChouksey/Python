# print kite shape design
for i in range(9):
    for j in range(9):
        if i==4 or j==4 or i+j==4 or i+j==12:
            print("* ",end=" ")
        elif (i==3 or i==7) and i+j==10:
            print("* ",end=" ")
        elif (i==2 or i==6) and i+j==8:
            print("* ",end=" ")
        elif (i==1 or i==5) and i+j==6:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()

