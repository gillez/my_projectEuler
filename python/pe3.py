
# The prime factors of 13195 are 5,7,13, and 29.

# What is the largest prime factor of the number
# 600,851,475,143?
# Answer is 6857

import time
import math
start_time = time.time()

target = 600851475143
largest = 0

def isPrime(x):
    prime = True
    for i in range(3, x - 1, 2):
        if (x % i) == 0:
            prime = False
            break
    return prime

factors = []

# Solution 1: Reduce the max iter to the pair of the factor each time we find one
# maxIter = math.floor(target / 2) + 1
# x = 3
# while x < maxIter:
#     if (target % x) == 0:
#         factors.append(x)
#         # We don't need to iter past the opposite factor.
#         maxIter = math.floor(target / x)
#         factors.append(maxIter)
#     x = x + 1

# Solution 1: We only need to iter up to the square root of the target
maxIter = math.floor(math.sqrt(target)) + 1
print("maxIter (sqrt of {0} + 1): {1}".format(target, maxIter))
for x in range(3, maxIter, 2):
    if (target % x) == 0:
        factors.append(x)
        # Also append the pair of the factor.
        pair = math.floor(target / x)
        if x != pair:
            factors.append(math.floor(target / x))

factors.sort(reverse=True)
print("Factors", factors)
for x in factors:
    if isPrime(x):
        largest = x
        break

print(largest)

print(f"--- Number of seconds to solve {time.time() - start_time}")
