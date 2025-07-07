# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 0123 0132 0213 0231 0312 0321 1023 1032 1203 1230 1302 1320 2013 2031 2103 2130 2301 2310 3012 3021 3102 3120 3201 3210




import time
import math

start_time = time.time()

answer = 0

answerDigits = []
target = 1000000
numDigits = 10
# target = 9
# numDigits = 4

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
factorials = [0, 1]

for i in range(2, numDigits):
    factorials.append(factorials[i-1] * i)

# my solution below gets one position after the answer, I guess we're effectively starting the count from 0...
# I should be able to work this out but the easy solution for now is just to reduce the target by 1.
target -= 1

for i in range(numDigits-1, 0, -1):
    idx = math.floor(target / factorials[i])
    answerDigits.append(digits[idx])
    digits.pop(idx)
    target = target % factorials[i]

answerDigits.append(digits[0])
print(answerDigits)
answer = int(''.join(map(str, answerDigits)))

print(f"answer: {answer}")
print(f"--- Number of seconds to solve {time.time() - start_time}")
