#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract the AM/PM part and the hour
    period = s[-2:]
    hour = int(s[:2])
    minutes_seconds = s[2:8]

    # Convert based on AM/PM
    if period == "AM":
        if hour == 12:
            hour = 0  # Midnight case
    else:  # PM case
        if hour != 12:
            hour += 12  # Convert PM hour to 24-hour format

    # Format the hour to be two digits and return the converted time
    return f"{hour:02}{minutes_seconds}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
