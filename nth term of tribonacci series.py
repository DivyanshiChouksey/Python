#nth term of tribonacci series
a = 0
b = 1
c = 1
n = int(input("enter nth term "))
if n== 0:
    print("0")
if n==1 or n==2:
    print("1")
for i in range(0,n-2):
    next = a+b+c
    a = b
    b = c
    c = next
print(next)
