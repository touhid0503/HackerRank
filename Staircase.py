#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    # Write your code here
    for i in range(n):
        for k in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print()


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
