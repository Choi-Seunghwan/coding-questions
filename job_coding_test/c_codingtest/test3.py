#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'prefixToPostfix' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY prefixes as parameter.
#

def prefixToPostfix(prefixes):
    # Write your code here
    results = []

    for prefix in prefixes:
        st = []
        for ch in reversed(prefix):
            if ch.isdigit():
                st.append(ch)
            else:
                val1 = st.pop()
                val2 =st.pop()
                new_val = str(val1) + str(val2) + str(ch)
                st.append(new_val)
        results.append(st.pop())
        
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    prefixes_count = int(input().strip())

    prefixes = []

    for _ in range(prefixes_count):
        prefixes_item = input()
        prefixes.append(prefixes_item)

    result = prefixToPostfix(prefixes)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
