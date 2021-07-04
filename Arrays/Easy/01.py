"""
Dynamic Array
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    two_dimensional_array = [[] for _ in range(n)]
    last_answer = 0
    result = []

    for query in queries:
        operation, x, y = query
        index = (x ^ last_answer) % n

        if operation == 1:
            two_dimensional_array[index].append(y)
        else:
            position = y % len(two_dimensional_array[index])
            last_answer = two_dimensional_array[index][position]
            result.append(last_answer)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
