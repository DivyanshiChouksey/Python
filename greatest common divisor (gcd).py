# greatest common divisor (gcd)
a = 3918848
b = 1653264
while a%b !=0:
     mod = a%b
     a = b
     b = mod
print(b)
