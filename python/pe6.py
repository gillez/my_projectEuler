# The sum of the squares of the first ten natural numbers
# is 1^2 + 2^2 + 3^2... = 385
# The square of the sum of the first ten natural numbers
# is (1 + 2 + 3 + 4...)^2 == 55^2 = 3025,
# Hence the difference between the sum of the squares
# of the first ten natural numbers and the square of the
# sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square
# of the sum.

import time
import math
start_time = time.time()

def sumSquares(end):
	sum = 0
	for i in range(1, end+1):
		sum += i ** 2
	return sum

def squareSum(end):
	sum = 0
	for i in range(1, end+1):
		sum += i
	return sum ** 2

end = 100
print(squareSum(end) - sumSquares(end))

print(f"--- Number of seconds to solve {time.time() - start_time}")
