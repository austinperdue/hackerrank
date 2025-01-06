#!/bin/python3
# Austin Perdue

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
# INPUT FORMAT
# The first line contains an integer n, the number of integers in array a.
# The second line contains n space-separated integers that describe a.
# OUTPUT
# Print all n integers in a in reverse order as a single line of space-separated integers.

def reverseArray(a):
    
    # Write your code here

    # can also do return a[::-1] (slicing)
    
    # python reverse function (returns None)
    a.reverse()
    
    # return reversed list
    return a
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
