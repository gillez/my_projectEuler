# 2^15 is 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000

import time
import math

start_time = time.time()

strnum = str(pow(2, 1000))
total = 0

print(strnum)

for c in strnum:
    total += int(c)

print(f"total {total}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


