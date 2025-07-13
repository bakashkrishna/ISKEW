#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N, num=1):
    # Write your code here
    value=num**N
    if value>X:
        return 0
    elif value==X:
        return 1
    else:
        return powerSum(X-value,N,num+1)+powerSum(X,N,num+1)

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input("Number X:").strip())

    N = int(input("Power N:").strip())

    result = powerSum(X, N)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
