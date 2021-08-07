def findPrimes(characters_min, characters_max, maximum_primes='0'):
	maximum_primes_set = False
	if maximum_primes != 0: maximum_primes_set = True
	primes_list = []
	def isPrime(number):
		if number > 1:
			for discriminator in range(2, int(number**0.5) + 1):
				if (number % discriminator) == 0:
					return False
			return True
		elif number == 1: return True
	start_point = '1'
	end_point = '9'
	for _ in range(characters_min - 1):
		start_point += '0'
	for _ in range(characters_max - 1):
		end_point += '9'
	start_point = int(start_point)
	end_point = int(end_point)
	for prime_candidate in range(start_point, end_point + 1):
		if maximum_primes_set:
			if len(primes_list) == maximum_primes: break
		if isPrime(prime_candidate): primes_list.append(prime_candidate)
	return(primes_list)