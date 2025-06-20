# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into ).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1,2,4,,71, and 142;
# so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time
import math

start_time = time.time()

answer = 0
max = 10000

sums = [0, 0]

def sumOfDividers(target):
    sum = 1
    maxIter = math.floor(math.sqrt(target))
    for x in range(2, maxIter, 1):
        if ((target % x) == 0):
            sum += x
            if ((target / x) != x):
                sum += target / x
    return sum

for num in range(2, 10000):
    sums.append(sumOfDividers(num))

for num in range(2, 10000):
    if ((sums[num] < 10000) and (sums[num] > num) and (sums[int(sums[num])] == num)):
        print(f"Amicable pair: {num} and {sums[num]}")
        answer += num
        answer += sums[num]

print(f"{answer}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


