#fibonacci
a = 0
b = 1
print("0")
print("1")
for i in range(0,10) :
    next = a + b
    print(next)
    a = b
    b = next
