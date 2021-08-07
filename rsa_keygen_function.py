import math, sys

def RSAKeygen(prime_one, prime_two, x):
	def isPrime(number):
		if number > 1:
			for discriminator in range(2, number):
				if (number % discriminator) == 0:
					return False
			return True
		elif number == 1: return True

		if not isPrime(prime_one) and not isPrime(prime_two):
			return_string = str(prime_two) + ' is not a prime! Halting...'
			return(return_string)
		elif not isPrime(prime_one) and isPrime(prime_two):
			return_string = str(prime_one) + ' is not a prime! Halting...'
			return(return_string)
		elif isPrime(prime_one) and not isPrime(prime_two):
			return_string = str(prime_one) + ' and ' + str(prime_two) + ' are not primes! Halting...'
			return(return_string)

	phi = (prime_one - 1) * (prime_two - 1) + 1

	y = int(1)
	xy = x*y

	while y == 1:
		while xy != phi:
			x += 1
			y = int(phi / x)
			xy = x * y
			xy = xy
		pq = prime_one * prime_two
		list_keygen_params = [x, y, pq]
	return(list_keygen_params)