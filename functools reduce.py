from functools import reduce
lst  = [1,2,3,4,5]
mul = reduce(lambda x,y: x*y,lst)
print(mul)
