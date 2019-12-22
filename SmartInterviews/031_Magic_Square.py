# https://www.hackerrank.com/challenges/magic-square-forming/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# using inbuilt librabry to generate permutations
from itertools import permutations 

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    perms = permutations(range(1,10),9)
    min_ans = sys.maxsize
  
    for tuple1 in perms:
        if (tuple1[0]+tuple1[1]+tuple1[2] == \
        tuple1[3]+tuple1[4]+tuple1[5] == \
        tuple1[6]+tuple1[7]+tuple1[8]== \
        tuple1[0]+tuple1[3]+tuple1[6] == \
        tuple1[1]+tuple1[4]+tuple1[7] == \
        tuple1[2]+tuple1[5]+tuple1[8]== \
        tuple1[0]+tuple1[4]+tuple1[8] == tuple1[2]+tuple1[4]+tuple1[6]):
      
            magic_square = [[tuple1[0], tuple1[1], tuple1[2]], \
            [tuple1[3], tuple1[4], tuple1[5]],\
            [tuple1[6], tuple1[7], tuple1[8]]]
      
            cost = 0
      
            for i in range(0,3):
                for j in range(0,3):
                    if s[i][j] != magic_square[i][j]:
                        cost += abs(s[i][j] - magic_square[i][j])
            
            if min_ans > cost:
                min_ans = cost
    return min_ans


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    
    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
