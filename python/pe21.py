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

max = 287

# Used for both solutions to find and add amicable pairs.
def sumAmicable(sums):
    answer = 0
    for num in range(2, max):
        if ((sums[num] < num) and (sums[int(sums[num])] == num)):
            print(f"Amicable pair: {num} and {sums[num]}")
            answer += num
            answer += sums[num]
    return answer

# solution 1: loop to sqrt(target) and add factors

sums = [1] * max

def sumOfDividers(target):
    sum = 1
    maxIter = int(math.sqrt(target))
    for x in range(2, maxIter):
        if ((target % x) == 0):
            sum += x
            if ((target / x) != x):
                sum += target / x
    return sum

for num in range(2, max):
    sums[num] = sumOfDividers(num)

answer = sumAmicable(sums)

print(f"solution 1 (calc factors): {answer}")

print(f"--- Number of seconds to solve {time.time() - start_time}")

# solution 1: sieve solution
# Note, this is the fastest sieve solution given on the Udemy video, however, I have
# realised that, although it given the correct answer in our case it's not quite
# correct! If you reduce max to 285, the answers are not the same! This is
# it doesn't calculate the last few numbers correctly, probably due to rounding when
# calculatng int(math.sqrt(max)) and int(max/i)
start_time = time.time()

sums = [1] * max

for i in range(2, int(math.sqrt(max))):
    for j in range(i, int(max/i)):
        sums[i*j] += i + j

answer = sumAmicable(sums)

print(f"solution 2 (sieve): {answer}")

print(f"--- Number of seconds to solve {time.time() - start_time}")
