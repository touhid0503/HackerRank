#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    res=[]
    for i in range(p,q+1):
        s=str(i*i)
        n=len(s)
        if i==1:
            res.append(i)
        elif n>1 and i == int(s[:n//2])+int(s[n//2:]):
            res.append(i)
    if len(res)==0:
        print("INVALID RANGE")
    else:
        print(*res)
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
