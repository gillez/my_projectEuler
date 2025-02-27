# n! means n * (n-1) * (n-2)  * ... * 2 * 1
# For example, 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362880
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 = 27
#
# Find the sum of the digits in the number 100!

import time
import math

start_time = time.time()

value = str(math.factorial(100))
answer = 0
for d in value:
    answer += int(d)

print(f"Sum of digits in 100! is {answer}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


