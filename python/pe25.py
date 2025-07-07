# The Fibonacci sequence is defined by the recurrence relation:
# fN = fN-1 + fN-2, where f1 = 1 and f2 = 1,
# Hence the first 12 terms will be:
#   f1 = 1,
#   f2 = 1,
#   f3 = 2,
#   f4 = 3,
#   f5 = 5,
#   f6 = 8,
#   f7 = 13,
#   f8 = 21,
#   f9 = 34,
#   f10 = 55,
#   f11 = 89,
#   f12 = 144

# The 12th term, f12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?

import time
import math

start_time = time.time()

answer = 0


print(f"answer: {answer}")
print(f"--- Number of seconds to solve {time.time() - start_time}")
