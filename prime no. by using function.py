a  = int(input("Enter a number "))
def isprime(a):
	for i in range(2,int(a**0.5)+1):
			if a % i == 0 :
				return "this number is not a prime number"
			return "this number is a prime number"
print(isprime(a))
    