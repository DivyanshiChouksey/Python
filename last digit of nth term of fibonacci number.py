def fib(n) :
    n = n%60
    fibs = [0,1]
    f1 = 0
    f2 = 1
    for i in range (2,n+1):
        f1,f2 = f2,f1+f2
    return f2
out = fib(185)
print(out)


# def fib(n) :
#     n = n%60
#     fibs = [0,1]
#     for i in range (2,n+1):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs[-1]

# out = fib(185)
# print(out)