a=int(input("Enter a number "))
def isprime(a):
	for i in range(2,a) :
			if a%i==0 :
				print("not a prime no.")
				break	
			elif 1 + i == a :
					print("prime number")

isprime(a)
    