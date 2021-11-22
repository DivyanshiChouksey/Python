def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f * i
    return (f)


a = 5
b = 3
num1 = fact(a)
num2 = fact(a-b)
print(num1/num2)

 