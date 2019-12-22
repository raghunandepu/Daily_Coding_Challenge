#https://www.hackerrank.com/challenges/sock-merchant/problem
"""John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is 2."""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counts = dict()
    result = 0
    for i in ar:
        try:
            counts[i] += 1
        except:
            counts[i] = 1
    for k in counts.keys():
        result +=  (counts[k] // 2)
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')
    print(str(result)+'\n')

    #fptr.close()
