# LCM O(log(mn)) Time Complexity | O(1) Space complexity
def gcd(a,b):
    while a%b!=0:
        mod = a%b
        a = b
        b = mod
        return b
        
x = 24
y = 18
print(x*y//gcd(x,y)) #LCM 



# O(m*n) Time Complexity | O(1)Space complexity
x = 24
y = 18
greater = max(x,y)
while(True):
    if((greater % x == 0) and (greater % y == 0)) :
        lcm = greater
        break
    greater += 1
print(lcm)
