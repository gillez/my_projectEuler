# Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example,
# 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which
# a + b + c = 1000
# Find the product abc.


import time
import math
start_time = time.time()

product = 0
iterations = 0

def find_product():
    global iterations
    for a in range(1, 334):
        for b in range(a+1, 501-a):
            iterations += 1
            c = 1000 - a - b
            if (a * a) + (b * b) == (c * c):
                print(f"a = {a}, b = {b}, c = {c}, a + b + c = {a+b+c}, {a * a} + {b * b} = {c * c}, a * b * c = {a * b * c}")
                return a * b * c

product = find_product()
print(product)
print("Iterations", iterations)

print(f"--- Number of seconds to solve {time.time() - start_time}")
