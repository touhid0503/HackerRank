#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minimum=scores[0]
    maximum=scores[0]
    countmin=countmax=0
    for i in range(1,len(scores)):
        if minimum>scores[i]:
            minimum=scores[i]
            countmin+=1
        if maximum<scores[i]:
            maximum=scores[i]
            countmax+=1
    return countmax,countmin
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
