#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
# 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called
# abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2+ 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
# all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
# upper limit cannot be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time
import math

start_time = time.time()

max = 28123

answer = 0

start_time = time.time()

sums = [1] * max

# Use a sieve to find all the divisors

for i in range(2, math.ceil(math.sqrt(max))):
    sums[i*i] += i
    for j in range(i + 1, int(max/i)):
        sums[i*j] += i + j

# for i in range(2, max):
#     print("sums", i, sums[i])

abundantNumbers = []

# Find all abundant numbers
for i in range(2, max):
    if sums[i] > i:
        abundantNumbers.append(i)

numAbundant = len(abundantNumbers)
flags = [1] * max
halfMax = max / 2

abundantIter = int(numAbundant / 2)
if abundantNumbers[abundantIter] > halfMax:
    while abundantNumbers[abundantIter] > halfMax:
        abundantIter -= 1
else:
    while abundantNumbers[abundantIter] <= halfMax:
        abundantIter += 1

print("numAbundant", numAbundant, "abundantIter", abundantIter + 1)
for i in range(0, abundantIter + 1):
    for j in range(i, numAbundant):
        tot = abundantNumbers[i] + abundantNumbers[j]
        if tot < max:
            flags[tot] = 0

for i in range(1, max):
    if flags[i] == 1:
        answer += i

# Go through each pair of numbers and add together.
print(f"answer: {answer}")
print(f"--- Number of seconds to solve {time.time() - start_time}")
