# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, 13, we can see that the 6th prime is 13
# What is the 10,001st prime number?
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million.

import time
import math
start_time = time.time()

NUM = 2000000
primeTable = [True] * NUM

total = 0
numprimes = 0
sqrt_num = math.floor(math.sqrt(NUM))

for i in range(2, sqrt_num):
    if primeTable[i]:
        numprimes += 1
        total += i
        for j in range(i * i, NUM, i):
            primeTable[j] = False

for i in range(sqrt_num + 1, NUM):
    if primeTable[i]:
        numprimes += 1
        total += i

print(total)
print("Num primes", numprimes)

print(f"--- Number of seconds to solve {time.time() - start_time}")

