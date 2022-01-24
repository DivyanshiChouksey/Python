# print design of a triangle
for i in range(6):
    print("* "*i)


# method 2
for i in range(5):
    for j in range(5):
        if i>=j:
            print("*",end=" ")
    print()
