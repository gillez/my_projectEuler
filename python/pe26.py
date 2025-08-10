# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:
#   1/2 = 0.5
#   1/3 = 0.(3)
#   1/4 = 0.25
#   1/5 = 0.2
#   1/6 = 0.1(6)
#   1/7 = 0.(142857)
#   1/8 = 0.125
#   1/9 = 0.(1)
#   1/10 = 0.1

# Where 0.1(6) means 0.1666666--- and has a 1-digit recurring cycle.
# It can be seen that 1/7  has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

import time
import math

start_time = time.time()
answer = 0

FIRST=14
LIMIT=15
max_recurring = 0
dec = ""

def calcString(digits, rem, remainder):
    result = "0."

    # print("digits", digits)
    # print("remainder", remainder)
    # print("rem", rem)

    if rem == 0:
        result = result + "".join(map(str, digits))
    else:
        idx = len(digits) - len(remainder)
        result = result + "".join(map(str, digits[0:idx]))
        result = result + "(" + "".join(map(str, digits[idx::])) + ")"

    return result


for i in range(FIRST, LIMIT):
    remainder = []
    digits = []
    complete = False
    val = 10
    rem = 0

    # print("Calculating", i)

    while not complete:
        div = math.floor(val / i)
        rem = val % i
        # print(f"{val} / {i} = {div}, rem {rem}")
        if rem == 0:
            digits.append(div)
            complete = True
        elif rem in remainder:
            if div != digits[remainder.index(rem)]:
                # print("Add final digit")
                digits.append(div)
            complete = True
        else:
            digits.append(div)
            remainder.append(rem)
            val = rem * 10

    # print(f"1/{i}: {calcString(digits, rem, remainder)}")

    if rem != 0 and len(remainder) > max_recurring:
        max_recurring = len(remainder)
        answer = i
        print(f"new max: {answer}, length recurring {len(remainder)}, 1/{answer}: {calcString(digits, rem, remainder)}")


print(f"answer: {answer}")
print(f"--- Number of seconds to solve {time.time() - start_time}")
