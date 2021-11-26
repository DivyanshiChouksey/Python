# Greatest Common Divisor
# O(log(mn)) Time complexity | O()Space complexity
a = 3918848
b = 1653264  # smallest always
while a%b != 0: 
     mod = a%b
     a = b
     b = mod
print(b)


# O(m+n) Time Complexity | O(1) Space complexity
a = 98
b = 56
gcd = 1
for d in range(1,a+b) :
     if a%d == 0 and b%d == 0 :
          gcd = max(gcd,d)
print("The GCD of",a,"and",b,"is",gcd)


