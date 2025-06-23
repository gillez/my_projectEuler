# Using names.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by
# its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

import sys
sys.path.insert(1, '../../practical_algorithms/')

import time
import math
from radixPE22 import radix_sort

start_time = time.time()

def nameValue(name):
    total = 0
    base = ord('A') - 1

    for c in name:
        total += ord(c) - base
    return total

# File handling and sorting code taken from practical algorithms. I didn't write this.
names_file = open('../0022_names.txt')
# read file into a string and split into a list
names = names_file.read().split(',')
names_file.close() #good practice
# parse our list so the " are gone!
names = [name.strip('"') for name in names]
# and sort it
sorted_names = radix_sort(names)
# sorted_names = sorted(names) #sorted is the default python sort

# print(sorted_names)

answer = 0

for pos, name in enumerate(sorted_names):
    answer += (pos + 1) * nameValue(name)


print(f"answer: {answer}")
print(f"--- Number of seconds to solve {time.time() - start_time}")
