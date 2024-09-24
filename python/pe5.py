
# Find the smallest positive number which divides exactly by all the numbers 1-20.

import time
import math
start_time = time.time()

largest = 20
smallest = math.floor(largest / 2) + 1
found = False

def check_factors(num):
	for i in range(smallest, largest):
		if num % i:
			return False
	return True

num = largest
while not found:
	num += largest
	if check_factors(num):
		found = True

print(num)

print(f"--- Number of seconds to solve {time.time() - start_time}")
