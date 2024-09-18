# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6,and 9. The sum of these multiples is 23.
## natural numbers = non-negative integers. 1-9, integers

import time
start_time = time.time()

# Find the sum of all the multiples of 3 or 5 below 1000.
sum_total = 0 #init sum of our multiples if 3 or 5

#loop up to 1000
# for x in range (1, 1000):
#    if (x % 3 == 0 ) or (x % 5 == 0):
#        sum_total += x

#using add rather than mod
for x in range(3, 1000, 3):
    sum_total += x

x = 5
while x < 1000:
    sum_total += x
    x += 5
    if x < 1000:
        sum_total += x
        x += 10

print(sum_total)
print(f"--- Number of seconds to solve {time.time() - start_time}")
