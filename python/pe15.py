# Starting in the top left corner of a 2x2 grid,
# and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
# [
    # [1,1,1],
    # [1,2,3],
    # [1,3,6]
# ]

import time
import math

start_time = time.time()
SIZE = 20
VERTICES = SIZE + 1

# Shorthand to make 2d list.
#arr2d = [[1 for i in range(SIZE + 1)] for j in range(SIZE + 1)]
arr2d = []
for i in range(0, VERTICES):
    arr2d.append([1] * VERTICES)

for i in range(1, VERTICES):
    for j in range(1, VERTICES):
        arr2d[i][j] = arr2d[i][j - 1] + arr2d[i - 1][j]

print(f"size {SIZE}, paths {arr2d[SIZE][SIZE]}")

print(f"--- Number of seconds to solve {time.time() - start_time}")


