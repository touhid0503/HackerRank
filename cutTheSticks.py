#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def cutTheSticks(arr):
    # Write your code here

    res = []

    while arr:
        res.append(len(arr))
        x = min(arr)
        newarr = []
        for i in arr:
            if i > x:
                newarr.append(i - x)
        arr = newarr

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
