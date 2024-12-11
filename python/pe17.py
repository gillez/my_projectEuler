# If the numbers1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

import time
import math

start_time = time.time()
MAX=1000
RANGE=MAX
if MAX<1000:
    RANGE += 1

digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

digitsSize = []
for dig in digits:
    digitsSize.append(len(dig))
teensSize = []
for teen in teens:
    teensSize.append(len(teen))
tensSize = []
for ten in tens:
    tensSize.append(len(ten))

numchars = 0
for i in range(1, RANGE):
    # print(f"i {i}")
    hundreds = math.floor(i / 100)
    num = i % 100
    if hundreds > 0:
        numchars += digitsSize[hundreds] + 7     # "hundred"
        # print(f"HUNDREDS: i {i}, hundeds {hundreds} numchars {numchars}")
        if num > 0:
            numchars += 3   # "and"
            # print(f"AND: i {i}, numchars {numchars}")

    if num > 10 and num < 20:
        numchars += teensSize[num - 10]
        # print(f"TEENS: i {i}, numchars {numchars}")
    else:
        tens = math.floor(num / 10)
        numchars += tensSize[tens]
        # print(f"TENS: i {i}, num {tens} numchars {numchars}")
        num = num % 10
        numchars += digitsSize[num]
        # print(f"DIGITS: i {i}, num {num} numchars {numchars}")

if MAX == 1000:
    numchars += len("onethousand")


print(f"numchars {numchars}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


