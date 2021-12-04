def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner

def num():
    return 10

result = decor(num)
print(result())
