# tower of Hanoi (recursion)
def towerOfHanoi(n,a,c,b):
    if n == 1 :
        print("Move",n,"from",a,"to",c)
    else :
        #move n-1 rings from a to b using c 
        towerOfHanoi(n-1,a,b,c)
        print("Move",n,"from",a,"to",c)
        towerOfHanoi(n-1,b,c,a)

towerOfHanoi(3,'a','c','b')
