# The following iterative sequence is defined for the set of positive integers:
#    n -> n/2 (n is even)
#    n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
# finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
import math

start_time = time.time()

longest = 1
longest_start = 1

for i in range(2, 1000000):
  num = i
  length = 1
  while num != 1:
    if (num % 2):
      num = (3 * num) + 1
    else:
      num = num / 2
    length = length + 1

  if (length > longest):
    longest = length
    longest_start = i

print(f"longest_start {longest_start} length {longest}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


