# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, 13, we can see that the 6th prime is 13
# What is the 10,001st prime number?

import time
import math
start_time = time.time()

primes = [2, 3, 5, 7, 11, 13]
count = len(primes)
next = primes[len(primes) - 1]

def isPrime(x):
    global primes
    prime = True
    for i in primes:
        if (x % i) == 0:
            prime = False
            break
    return prime


while count != 10001:
	next += 2
	if isPrime(next):
		primes.append(next)
		count += 1

print(next)

print(f"--- Number of seconds to solve {time.time() - start_time}")
