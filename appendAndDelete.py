#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    c = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            c += 1
        else:
            break
    d = len(s) - c
    a = len(t) - c
    n = d + a
    if k >= n and (k - n) % 2 == 0 or k>=len(s)+len(t):
        return "Yes"
    else:
        return "No"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
