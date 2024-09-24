# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.

import time
import math
start_time = time.time()

product = 0
largest = [0, 0, 0]
numPalindromes = 0

def isPalindrome(i):
	global numPalindromes

	as_string = str(product)
	rev = as_string[slice(None, None, -1)]
	if as_string == rev:
		numPalindromes = numPalindromes + 1
		return True
	return False

for i in range(999, 99, -1):
	for j in range(i,99, -1):
		product = i * j
		if product > largest[0]:
			if isPalindrome(product):
				print("Found palindrome", i, j, "=", product)
				largest = [product, i, j]
				break
		else:
			break

print(largest)
print("Num palindromes checked", numPalindromes)

print(f"--- Number of seconds to solve {time.time() - start_time}")
