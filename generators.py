# generators
def arr(a,b):
    while a < b:
        yield a
        a+=1

g = arr(5,10)
for i in g:
    print(i)
