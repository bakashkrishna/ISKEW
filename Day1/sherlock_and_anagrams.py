#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    freq = {}
    count = 0

    for length in range(1,len(s)):
        for i in range(len(s)-length+1):
            substr=''.join(sorted(s[i:i+length]))
            if substr in freq:
                freq[substr]+=1
            else:
                freq[substr]=1

    for f in freq.values():
        if f>1:
            count+=(f*(f-1))//2

    return count
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("Enter the no of strings:").strip())

    for q_itr in range(q):
        s = input("Enter a string:").strip()

        result = sherlockAndAnagrams(s)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
